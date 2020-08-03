# Copyright 2020 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# For further info, check https://github.com/canonical/charmcraft

import textwrap
from unittest.mock import patch

from charmcraft.main import COMMAND_GROUPS
from charmcraft.help import get_full_help
from tests.factory import create_command


def test_default_help_text():
    """All different parts for the default help."""
    cmd1 = create_command('cmd1', 'Cmd help which is very long but whatever.', common_=True)
    cmd2 = create_command('command-2', 'Cmd help.', common_=True)
    cmd3 = create_command('cmd3', 'Extremely ' + 'super crazy long ' * 5 + ' help.', common_=True)
    cmd4 = create_command('cmd4', 'Some help.')
    cmd5 = create_command('cmd5', 'More help.')
    cmd6 = create_command('cmd6-really-long', 'More help.', common_=True)
    cmd7 = create_command('cmd7', 'More help.')

    command_groups = [
        ('group1', 'help text for g1', [cmd6, cmd2]),
        ('group3', 'help text for g3', [cmd7]),
        ('group2', 'help text for g2', [cmd3, cmd4, cmd5, cmd1]),
    ]
    fake_summary = textwrap.indent(textwrap.dedent("""
        This is the summary for
        the whole program.
    """), "    ")
    global_options = [
        ('-h, --help', 'Show this help message and exit.'),
        ('-q, --quiet', 'Only show warnings and errors, not progress.'),
    ]

    with patch('charmcraft.help.SUMMARY', fake_summary):
        text = get_full_help(command_groups, global_options)

    # XXX Facundo 2020-07-30: As we're losing the "regular summary"...
    #     usage: charmcraft [-h] [-v | -q] {version,build,init,lo...
    # ...we're not expressing that -v and -q are mutually exclusive.
    expected = textwrap.dedent("""\
        Usage:
            charmcraft [help] <command>

        Summary:
            This is the summary for
            the whole program.

        Global options:
            -h, --help:        Show this help message and exit.
            -q, --quiet:       Only show warnings and errors, not progress.

        Starter commands:
            cmd1:              Cmd help which is very long but whatever.
            cmd3:              Extremely super crazy long super crazy long super
                               crazy long super crazy long super crazy long
                               help.
            cmd6-really-long:  More help.
            command-2:         Cmd help.

        Commands can be classified as follows:
            group1:            cmd6-really-long, command-2
            group2:            cmd1, cmd3, cmd4, cmd5
            group3:            cmd7

        For more information about a command, run 'charmcraft help <command>'.
        For a summary of all commands, run 'charmcraft help --all'.
    """)
    assert text == expected


def test_aesthetic_help_msg():
    """All the real commands help msg start with uppercase and ends with a dot."""
    for _, _, commands in COMMAND_GROUPS:
        for cmd in commands:
            msg = cmd.help_msg
            assert msg[0].isupper() and msg[-1] == '.'


def test_aesthetic_args_options_msg():
    """All the real commands args/options help messages start and end with a dot."""
    fixme


# -- real execution outputs

def test_tool_exec_barenaked():
    """Execute charmcraft without any option at all."""
    fixme


def test_tool_exec_dash_help():
    """Execute charmcraft asking for help."""
    fixme


def test_tool_exec_command_incorrect():
    """Execute a command that doesn't exist."""
    fixme


def test_tool_exec_command_dash_help():
    """Execute a command asking for help."""
    fixme


def test_tool_exec_command_wrong_option():
    """Execute a correct command but with a wrong option."""
    fixme


def test_tool_exec_command_bad_option_type():
    """Execute a correct command but giving the valid option a bad value."""
    fixme
