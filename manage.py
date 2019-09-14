import pathlib
import random
import re
import string

from argcmdr import Local, localmethod
from descriptors import cachedproperty
from plumbum import colors
from plumbum.commands import ExecutionModifier


# TODO: add this to argcmdr...!

class _SHH(ExecutionModifier):
    """plumbum execution modifier to ensure output is not echoed to terminal
    essentially a no-op, this may be used to override argcmdr settings
    and cli flags controlling this feature, on a line-by-line basis, to
    hide unnecessary or problematic (e.g. highly verbose) command output.
    """
    __slots__ = ('retcode', 'timeout')

    def __init__(self, retcode=0, timeout=None):
        self.retcode = retcode
        self.timeout = timeout

    def __rand__(self, cmd):
        return cmd.run(retcode=self.retcode, timeout=self.timeout)


SHH = _SHH()

ROOT_PATH = pathlib.Path(__file__).parent

ENV_PATH = ROOT_PATH / '.env'

TEXTBOOK_PATH = ROOT_PATH / 'textbook'


def setup_env():
    """generate and set jupyter token in docker-compose environ"""
    try:
        env_text = ENV_PATH.read_text()
    except FileNotFoundError:
        env_text = ''

    if re.match(r'^JUPYTER_TOKEN=.+$', env_text, re.MULTILINE):
        return

    print(
        '[setup]' | colors.yellow,
        'one-time setup:',
        'generating docker-compose environment file',
        ENV_PATH,
    )

    token = ''.join(random.choices(string.ascii_letters + '*@!_-.', k=30))

    with ENV_PATH.open('a') as env_desc:
        if env_text and not env_text.endswith('\n'):
            env_desc.write('\n')

        env_desc.write(f'JUPYTER_TOKEN={token}\n')


def read_env():
    """read docker-compose environ file into dict"""
    try:
        env_text = ENV_PATH.read_text()
    except FileNotFoundError:
        env_text = ''

    return dict(
        line.split('=', 1)
        for line in env_text.splitlines()
        if '=' in line
    )


class Manage(Local):
    """manage the textbook-authoring environment"""

    @cachedproperty
    def compose(self):
        if self.args.execute_commands:
            setup_env()

        return self.local['docker-compose']

    @localmethod('--no-detach', dest='detach', default=True, action='store_false',
                 help="do not run containers in background")
    def start(self, args):
        """start development servers"""
        yield self.local.FG, self.compose[
            'up',
            ('-d',) if args.detach else (),
        ]

        if args.execute_commands and args.detach:
            environ = read_env()

            print()
            print('your jupyter development server is running at:' | colors.bold)
            print(
                '\n\t',
                f"http://localhost:8888/?token={environ['JUPYTER_TOKEN']}" | colors.underline,
            )
            print()
            print("edit textbook content there through the jupyter interface." | colors.info)

            print('\n')
            print('your textbook preview server is running at:' | colors.bold)
            print(
                '\n\t',
                "http://localhost:8008/jupyter-book/" | colors.underline,
            )
            print()
            print("preview the published result there prior to "
                  "committing and/or promoting." | colors.info)
            print()

    @localmethod
    def status(self):
        """list running development servers"""
        return self.local.FG, self.compose['ps']

    @localmethod('--destroy', action='store_true', help="tear down servers")
    def stop(self, args):
        """stop development servers"""
        if args.destroy:
            return self.compose['down']

        return self.compose['stop']

    @localmethod
    def build(self):
        """build textbook content for previewing and/or promoting"""
        return self.local.FG, self.compose[
            'exec',
            'jupyter',
            'jupyter-book',
            'build',
            'textbook',
        ]

    @localmethod('-y', '--yes', action='store_true',
                 help="do not prompt for confirmation")
    @localmethod('-f', '--force', action='store_true',
                 help="override restriction against uncommitted promotion")
    # TODO: @alias('publish')
    def promote(self, args):
        """publish textbook content on github.io"""
        if not args.force:
            (_retcode, git_status, _stderr) = yield SHH, self.local['git'][
                'status',
                '--short',
                TEXTBOOK_PATH,
            ]

            if git_status:
                print("uncommitted changes!" | colors.warn)
                print("hint: commit changes or specify flag -f / --force" | colors.bold)
                print()
                print('aborted' | colors.fatal)
                return

        if args.execute_commands and not args.yes:
            print('the latest committed textbook content will be '
                  'published to github.io' | colors.yellow)

            confirmed = None
            while confirmed not in ('y', 'yes', 'n', 'no'):
                confirmed = input(
                    ('continue? ' | colors.bold) +
                    '[y|yes|n|no]: '
                ).lower()

            print()

            if confirmed.startswith('n'):
                print('aborted' | colors.fatal)
                return

        # TODO: test
        yield self.local.FG, self.local['git'][
            'subtree',
            'push',
            '--prefix', 'textbook',
            'origin',
            'gh-pages',
        ]

        if args.execute_commands:
            print()
            print("SUCCESS" | colors.success)
            print()
            print("review the published textbook at:")
            # TODO: use pages.datascience.uchicago.edu (here and in README)?
            print("\n\t" + 'https://uchicagods.github.io/uchicagods/textbook-datascience-1/' + '\n')
            # TODO: could perhaps (optionally) poll the builds API to let user know status of build / when it's complete
