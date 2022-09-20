import json
import pathlib
import random
import re
import string
import time

from argcmdr import Local, localmethod, SHH
from descriptors import cachedproperty
from plumbum import colors


ROOT_PATH = pathlib.Path(__file__).parent

ENV_PATH = ROOT_PATH / '.env'

IMAGE_PATH = ROOT_PATH / 'image'

TEXTBOOK_PATH = ROOT_PATH / 'textbook'
PREVIEW_PATH = ROOT_PATH / 'preview'

REPO_OWNER = 'chicago-cdac'

REPO_NAME = 'textbook-datascience-1'

REPO_URI = f'https://github.com/{REPO_OWNER}/{REPO_NAME}'

REGISTRY_HOST = 'ghcr.io'


def setup_env():
    """generate and set jupyter token in environ"""
    try:
        env_text = ENV_PATH.read_text()
    except FileNotFoundError:
        env_text = ''

    if re.match(r'^JUPYTER_TOKEN=.+$', env_text, re.MULTILINE):
        return

    print(
        '[setup]' | colors.yellow,
        'one-time setup:',
        'generating environment file:',
        ENV_PATH,
    )

    token = ''.join(random.choices(string.ascii_letters + '*@!_-.', k=30))

    with ENV_PATH.open('a') as env_desc:
        if env_text and not env_text.endswith('\n'):
            env_desc.write('\n')

        env_desc.write(f'JUPYTER_TOKEN={token}\n')


def read_env():
    """read environ file into dict"""
    try:
        env_text = ENV_PATH.read_text()
    except FileNotFoundError:
        env_text = ''

    return dict(
        line.split('=', 1)
        for line in env_text.splitlines()
        if '=' in line
    )


def get_host():
    crostini_env = pathlib.Path('/etc/apt/sources.list.d/cros.list').exists()
    return 'penguin.linux.test' if crostini_env else 'localhost'


class Manage(Local):
    """manage the textbook-authoring environment"""

    image_name = 'textbook-jupyter-service'
    registry_uri = f'{REGISTRY_HOST}/{REPO_OWNER}/{image_name}'

    @cachedproperty
    def environ(self):
        if self.args.execute_commands:
            setup_env()

        return read_env()

    @localmethod('--no-pull', dest='pull', action='store_false',
                 help="do not pull latest image")
    @localmethod('--no-detach', dest='detach', action='store_false',
                 help="do not run containers in background")
    @localmethod('--name', default=image_name,
                 help="name to assign to container (default: %(default)s)")
    def start(self, args):
        """start development server"""
        token = self.environ.get('JUPYTER_TOKEN', 'TO-BE-DEFINED')

        if args.pull:
            yield self.local['docker'][
                'pull',
                f'{self.registry_uri}:latest',
            ]

        yield from self['stop'].prepare(args)

        yield self.local.FG, self.local['docker'][
            'run',
            '--rm',
            '--publish', '8888:8888',
            '--volume', f'{TEXTBOOK_PATH}:/home/jovyan/textbook',
            '--name', args.name,
            ('--detach',) if args.detach else (),
            f'{self.registry_uri}:latest',
            'start-notebook.sh',
            '--NotebookApp.notebook_dir=textbook',
            f'--NotebookApp.token={token}',
        ]

        if args.execute_commands and args.detach:
            hostname = get_host()

            print()
            print('your jupyter development server is running at:' | colors.bold)
            print(
                '\n\t',
                f"http://{hostname}:8888/?token={token}" | colors.underline,
            )
            print()
            print("edit textbook content there through the jupyter interface." | colors.info)

            print()
            print('to preview changes to the textbook see:' | colors.info,
                  'manage build' | colors.underline)

    @localmethod('--name', default=image_name,
                 help="name assigned to container (default: %(default)s)")
    def status(self, args):
        """list running development servers"""
        (retcode, stdout, _stderr) = yield SHH(retcode=None), self.local['docker'][
            'inspect',
            '--format', '{{json .State.Status}}',
            args.name,
        ]

        if retcode is None:
            return

        status = 'stopped' if retcode > 0 else json.loads(stdout)

        print(status)

    @localmethod('--name', default=image_name,
                 help="name assigned to container (default: %(default)s)")
    def restart(self, args):
        """restart development servers"""
        yield self.local['docker'][
            'restart',
            args.name,
        ]

    @localmethod('--name', default=image_name,
                 help="name assigned to container (default: %(default)s)")
    def stop(self, args):
        """stop development server"""
        yield SHH(retcode=None), self.local['docker'][
            'stop',
            args.name,
        ]

    @localmethod('--all', action='store_true',
                 help="build all pages "
                      "(regardless of whether they *appear* to have changed)")
    @localmethod('--no-pull', dest='pull', action='store_false',
                 help="do not pull latest image")
    def build(self, args):
        """build textbook content for local preview"""
        if args.pull:
            yield self.local['docker'][
                'pull',
                f'{self.registry_uri}:latest',
            ]

        yield self.local['docker'][
            'run',
            '--rm',
            '--volume', f'{TEXTBOOK_PATH}:/home/jovyan/textbook',
            '--volume', f'{PREVIEW_PATH}:/home/jovyan/preview',
            f'{self.registry_uri}:latest',
            'jupyter-book',
            'build',
            '--quiet',
            '--path-output', 'preview/',
            ('--all',) if args.all else (),
            'textbook',
        ]

        if args.execute_commands:
            path_html = PREVIEW_PATH / 'html'
            path_index = path_html / 'index.html'

            print()
            print('the textbook has been built at:' | colors.bold)
            print(
                '\n\t',
                str(path_html) | colors.underline,
            )
            print()
            print("open" | colors.info,
                  "index.html" | colors.underline,
                  "in your browser to preview:" | colors.info)
            print(
                '\n\t',
                f'file://{path_index}' | colors.underline,
            )
            print()

    class Image(Local):
        """manage the textbook-authoring docker image"""

        image_paths = frozenset(element.name for element in IMAGE_PATH.iterdir()
                                if element.is_dir())

        def __init__(self, parser):
            parser.add_argument(
                'target',
                choices=self.image_paths,
                help="image/ directory to build",
            )

        @cachedproperty
        def registry_uri(self):
            distro_name = f'textbook-{self.args.target}'
            return f'{REGISTRY_HOST}/{REPO_OWNER}/{distro_name}'

        @localmethod
        def build(self, args):
            """build a docker image"""
            timestamp_build = int(time.time())

            yield self.local['docker'][
                'build',
                '--label', f'org.opencontainers.image.source={REPO_URI}',
                '--tag', f'{self.registry_uri}:{timestamp_build}',
                '--tag', f'{self.registry_uri}:latest',
                IMAGE_PATH / args.target,
            ]

        @localmethod
        def push(self):
            """push a docker image to the registry"""
            yield self.local['docker'][
                'push',
                '--all-tags',
                self.registry_uri,
            ]
