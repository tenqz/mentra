"""Defines interface for CLI application."""

from abc import ABC, abstractmethod


class CLIInterface(ABC):
    """Protocol for CLI application classes."""

    @abstractmethod
    def run(self) -> int:
        """Execute the CLI application.

        Returns:
            int: Exit code (0 for success).

        """
        ...