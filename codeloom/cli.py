import sys

from codeloom import branding
from codeloom.args import get_parser


LIGHTWEIGHT_FLAGS = {"--help", "-h", "--version"}


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    if any(arg in LIGHTWEIGHT_FLAGS for arg in argv):
        parser = get_parser([], None)
        parser.prog = branding.CLI_NAME
        parser.parse_args(argv)
        return None

    from codeloom.main import main as runtime_main

    return runtime_main(argv)
