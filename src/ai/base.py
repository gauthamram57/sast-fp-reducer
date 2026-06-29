"""
Base interface for all AI providers.
"""

from abc import ABC, abstractmethod


class BaseAIClient(ABC):
    """
    Every AI provider must implement this interface.
    """

    @abstractmethod
    def chat(self, prompt: str) -> str:
        """
        Send a prompt to an AI provider.

        Returns:
            Raw string response.
        """
        pass
