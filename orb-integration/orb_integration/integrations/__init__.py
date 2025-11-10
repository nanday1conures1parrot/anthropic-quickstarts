"""Integration modules for different AI technologies."""

from .base import BaseIntegration
from .claude_integration import ClaudeIntegration
from .github_integration import GitHubIntegration
from .copilot_integration import CopilotIntegration
from .huggingface_integration import HuggingFaceIntegration

__all__ = [
    "BaseIntegration",
    "ClaudeIntegration",
    "GitHubIntegration",
    "CopilotIntegration",
    "HuggingFaceIntegration",
]
