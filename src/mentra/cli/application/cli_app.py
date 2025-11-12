"""Mentra CLI entry point module.

This module provides the entry class for the command-line interface (CLI).
It handles argument parsing and executes basic responses.
"""

import sys

from mentra.cli.application.interfaces.cli_interface import CLIInterface


class CLIApp(CLIInterface):
    """CLI application wrapper for Mentra commands."""

    def __init__(self, argv: list[str] | None = None) -> None:
        """Initialize CLIApp.

        Args:
            argv (list[str] | None): Optional list of arguments to parse.

        """
        self.argv = argv or sys.argv[1:]

    def run(self) -> int:
        """Run the CLI application.

        Parses arguments and prints 'ok' as a placeholder response.

        Returns:
            int: Exit code (0 for success).

        """
        print("ok")

        return 0
