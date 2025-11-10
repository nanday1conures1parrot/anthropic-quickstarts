"""Base integration class for all AI technology integrations."""

from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseIntegration(ABC):
    """
    Abstract base class for all technology integrations in the Orb system.

    Each integration represents a connection to an external AI service or tool,
    providing a unified interface for the Orb to interact with diverse systems.
    """

    def __init__(self, name: str, enabled: bool = True):
        """
        Initialize the integration.

        Args:
            name: Human-readable name of the integration
            enabled: Whether this integration is active
        """
        self.name = name
        self.enabled = enabled
        self._context: Dict[str, Any] = {}

    @abstractmethod
    async def process(self, unified_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process the unified input and return a response.

        Args:
            unified_input: The condensed input from the Orb core

        Returns:
            Response dictionary containing results from this integration
        """
        pass

    def set_context(self, context: Dict[str, Any]) -> None:
        """Update the integration's context."""
        self._context.update(context)

    def get_context(self) -> Dict[str, Any]:
        """Get the current context."""
        return self._context.copy()

    def is_enabled(self) -> bool:
        """Check if this integration is enabled."""
        return self.enabled

    def enable(self) -> None:
        """Enable this integration."""
        self.enabled = True

    def disable(self) -> None:
        """Disable this integration."""
        self.enabled = False
