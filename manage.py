import itertools
import json
import os
import pathlib
import random
import re
import string
import sys
import time

from argcmdr import Local, localmethod
from descriptors import cachedproperty
from plumbum import colors
from plumbum.commands import ExecutionModifier


# TODO: add _SHH to argcmdr!

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

TEXTBOOK_PATH = ROOT_PATH / 'textbook' / '_site'

ANSI_ERASE = "\033[K"
ANSI_UPN = "\033[{n}A"
ANSI_BACKN = "\033[{n}D"

BUILDS_URL = 'https://api.github.com/repos/uchicagods/textbook-datascience-1/pages/builds'


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
                "http://localhost:8008/" | colors.underline,
            )
            print()
            print("preview the published result there prior to "
                  "committing and/or promoting." | colors.info)
            print()

    @localmethod
    def status(self):
        """list running development servers"""
        return self.local.FG, self.compose['ps']

    @localmethod
    def restart(self):
        """restart development servers"""
        return self.local.FG, self.compose['restart']

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
    @localmethod('-r', '--rebased', action='store_true',
                 help="force push against remote history")
    @localmethod('--no-poll', action='store_false', default=True, dest='poll',
                 help="do not poll build status (polling requires environ variable "
                      "GH_CREDENTIALS with value of the form: "
                      '"my-user-name:my-password-or-token")')
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

        if args.execute_commands:
            build0 = yield from self._get_build()
        else:
            build0 = None

        relative_path = TEXTBOOK_PATH.relative_to(ROOT_PATH)
        prefix_args = ('--prefix', relative_path)

        if args.rebased:
            (_retcode, root_sha, _stderr) = yield SHH, self.local['git'][
                'subtree',
                'split',
                prefix_args,
            ]

            if root_sha is None:
                root_sha = 'DRY-RUN'
            else:
                # trim newline
                root_sha = root_sha.strip()

            yield self.local.FG, self.local['git'][
                'push',
                'origin',
                f'{root_sha}:gh-pages',
                '--force',
            ]
        else:
            try:
                yield self.local.FG, self.local['git'][
                    'subtree',
                    'push',
                    prefix_args,
                    'origin',
                    'gh-pages',
                ]
            except self.local.ProcessExecutionError:
                print()
                print('subtree-push failed' | colors.fatal)
                print()
                print("hint 1: make sure you've pulled remote changesets: git pull" |
                      colors.yellow)
                print()
                print("hint 2: or, if you're sure, force-push, with the manage-promote "
                      "flag: -r / --rebased" | colors.yellow)
                print()
                raise

        if args.execute_commands:
            print()
            print("SUCCESS" | colors.success)
            print()
            print("review the published textbook at:")
            print("\n\t" + ('https://ds1.datascience.uchicago.edu/' | colors.underline) + '\n')

            if args.poll and build0 is not None:
                build = yield from self._poll_until(build0, changed='url')

                _print_build_status(build)

                if build['status'] == 'building':
                    # NOTE: may need to test for ANSI capability?

                    # we've already printed two lines; go back to beginning to re-poll:
                    print(ANSI_UPN.format(n=2), end='')

                    # clear the line:
                    print(ANSI_ERASE, end='\r')

                    build1 = yield from self._poll_until(build, changed='status')

                    print(ANSI_ERASE, end='\r')
                    _print_build_status(build1)

    def _get_build(self):
        github_credentials = os.getenv('GH_CREDENTIALS')
        if not github_credentials:
            return None

        (_retcode, builds_out, _stderr) = yield SHH, self.local['curl'][
            '-u', github_credentials,
            BUILDS_URL,
        ]

        if builds_out is None:
            # dry run
            return None

        unexpected_message = (
            ("unexpected api response" | colors.fatal) +
            f"\n\nfrom {BUILDS_URL} --"
            f"\n\n{builds_out}"
        )

        try:
            builds = json.loads(builds_out)
            return builds[0]
        except IndexError:
            return {}
        except (TypeError, ValueError):
            print(unexpected_message)
            raise
        except KeyError:
            if builds.get('message') == "Not Found":
                print('unexpected response (Not Found) -- verify GH_CREDENTIALS' | colors.fatal)
            else:
                print(unexpected_message)
            raise

    def _poll_until(self, build0, changed):
        build = build0
        spinner = itertools.cycle('\|/-')

        sys.stdout.write('polling page build api ... ')
        sys.stdout.write(next(spinner))
        sys.stdout.flush()

        while build.get(changed) == build0.get(changed):
            if build is not build0:
                sys.stdout.write(ANSI_BACKN.format(n=1))
                sys.stdout.write(next(spinner))
                sys.stdout.flush()
                time.sleep(2)

            build = yield from self._get_build()

        print()
        return build


def _print_build_status(build):
    status = build['status']

    if status == 'building':
        status_colored = status | colors.yellow
    elif status == 'built':
        status_colored = status | colors.green
    elif status == 'errored':
        status_colored = status | colors.fatal
    else:
        status_colored = status

    print('status:', status_colored)

    if status == 'errored':
        print('message:', build['error']['message'])
