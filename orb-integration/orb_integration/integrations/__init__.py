"""Integration modules for different AI technologies."""

from .base import BaseIntegration
from .claude_integration import ClaudeIntegration
from .copilot_integration import CopilotIntegration
from .github_integration import GitHubIntegration
from .huggingface_integration import HuggingFaceIntegration

__all__ = [
    "BaseIntegration",
    "ClaudeIntegration",
    "GitHubIntegration",
    "CopilotIntegration",
    "HuggingFaceIntegration",
]
