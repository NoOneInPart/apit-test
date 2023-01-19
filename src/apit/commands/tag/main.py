from collections.abc import Iterable
from pathlib import Path

from ..common_cli_parser_arguments import add_path_argument
from ..common_cli_parser_arguments import add_verbose_argument
from .command import execute
from apit.cli_options import CliOptions
from apit.command_result import CommandResult


def setup_cli_parser(subparsers):
    tag_command = subparsers.add_parser(
        "tag",
        help="tag files in PATH",
        description="tag files in PATH using Apple Music metadata",
    )
    tag_command.set_defaults(func=main)

    add_verbose_argument(tag_command)
    tag_command.add_argument(
        "-b",
        "--backup",
        dest="has_backup_flag",
        action="store_true",
        default=False,
        help="create backup before updating tags (default: %(default)s)",
    )
    tag_command.add_argument(
        "-a",
        "--artwork",
        dest="has_embed_artwork_flag",
        action="store_true",
        help="download artwork to disk and save in files (default: %(default)s)",
    )
    tag_command.add_argument(
        "--artwork-size",
        dest="artwork_size",
        metavar="SIZE",
        type=int,
        default=600,
        help="set artwork size for download (default: %(default)s)",
    )
    add_path_argument(tag_command)
    tag_command.add_argument(
        "source",
        metavar="SOURCE",
        help="URL to Apple Music album for metadata download OR file with already downloaded metadata",  # noqa: B950
    )


def main(files: Iterable[Path], options: CliOptions) -> CommandResult:
    return execute(
        files=files,
        verbose_level=options.verbose_level,
        source=options.source,
        has_backup_flag=options.has_backup_flag,
        has_embed_artwork_flag=options.has_embed_artwork_flag,
        artwork_size=options.artwork_size,
    )
