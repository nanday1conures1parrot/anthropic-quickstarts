"""Claude AI integration for the Orb system."""

import os
from typing import Any, Dict, Optional

from anthropic import AsyncAnthropic

from .base import BaseIntegration


class ClaudeIntegration(BaseIntegration):
    """
    Integration with Claude AI for natural language understanding and generation.

    This integration connects to Anthropic's Claude API to provide advanced
    language model capabilities within the unified Orb system.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "claude-3-5-sonnet-20241022",
        enabled: bool = True,
    ):
        """
        Initialize the Claude integration.

        Args:
            api_key: Anthropic API key (defaults to ANTHROPIC_API_KEY env var)
            model: Claude model to use
            enabled: Whether this integration is active
        """
        super().__init__(name="Claude AI", enabled=enabled)
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.model = model
        self.client = AsyncAnthropic(api_key=self.api_key) if self.api_key else None

    async def process(self, unified_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process input through Claude AI.

        Args:
            unified_input: The condensed input from the Orb core

        Returns:
            Response dictionary with Claude's analysis and suggestions
        """
        if not self.client:
            return {
                "source": self.name,
                "status": "error",
                "message": "Claude API key not configured",
                "content": None,
            }

        try:
            # Extract the user's query
            query = unified_input.get("query", "")
            context = unified_input.get("context", {})

            # Build the prompt for Claude
            prompt = f"""You are part of a unified AI system called the Orb.

User Query: {query}

Context: {context}

Provide a comprehensive response that addresses the user's query. Your response will be
combined with insights from other AI systems (GitHub, Copilot, Hugging Face) to form a
unified answer."""

            # Call Claude API
            message = await self.client.messages.create(
                model=self.model, max_tokens=1024, messages=[{"role": "user", "content": prompt}]
            )

            # Extract response
            response_text = message.content[0].text if message.content else ""

            return {
                "source": self.name,
                "status": "success",
                "content": response_text,
                "model": self.model,
                "tokens_used": message.usage.input_tokens + message.usage.output_tokens,
            }

        except Exception as e:
            return {"source": self.name, "status": "error", "message": str(e), "content": None}
