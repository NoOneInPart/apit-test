from .list.main import setup_cli_parser as list_setup_cli_parser
from .tag.main import setup_cli_parser as tag_setup_cli_parser


def get_cli_parser_setups_fns():
    return [list_setup_cli_parser, tag_setup_cli_parser]
