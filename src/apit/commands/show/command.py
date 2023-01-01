from collections.abc import Iterable
from pathlib import Path

from .action import ReadAction
from apit.action import all_actions_successful
from apit.command import Command
from apit.command_result import CommandResult
from apit.report import print_report


class ShowCommand(Command):
    def execute(self, files: Iterable[Path], options) -> CommandResult:
        actions: list[ReadAction] = [ReadAction(file, {}) for file in files]

        for action in actions:
            print("Executing:", action)
            action.apply()

        print_report(actions)
        return (
            CommandResult.SUCCESS
            if all_actions_successful(actions)
            else CommandResult.FAIL
        )
