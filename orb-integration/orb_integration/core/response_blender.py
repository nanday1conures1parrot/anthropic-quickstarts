"""Response blender for the Orb system."""

from typing import Any, Dict, List


class ResponseBlender:
    """
    Response blender that unifies outputs from multiple integrations.

    This component takes responses from all integrated systems and blends them
    into a single coherent result that represents the collective intelligence
    of the Orb.
    """

    def __init__(self):
        """Initialize the response blender."""
        pass

    def blend_responses(
        self, responses: List[Dict[str, Any]], strategy: str = "weighted"
    ) -> Dict[str, Any]:
        """
        Blend multiple responses into a unified output.

        Args:
            responses: List of response dictionaries from different integrations
            strategy: Blending strategy ("weighted", "concatenate", or "prioritize")

        Returns:
            Unified response dictionary
        """
        if not responses:
            return {"status": "error", "message": "No responses to blend", "unified_content": None}

        # Filter successful responses
        successful = [r for r in responses if r.get("status") == "success"]
        failed = [r for r in responses if r.get("status") != "success"]

        if not successful:
            return {
                "status": "error",
                "message": "All integrations failed",
                "errors": [r.get("message") for r in failed],
                "unified_content": None,
            }

        # Apply blending strategy
        if strategy == "weighted":
            return self._weighted_blend(successful, failed)
        elif strategy == "concatenate":
            return self._concatenate_blend(successful, failed)
        elif strategy == "prioritize":
            return self._prioritize_blend(successful, failed)
        else:
            return self._weighted_blend(successful, failed)

    def _weighted_blend(
        self, successful: List[Dict[str, Any]], failed: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Blend responses with weighted importance.

        Args:
            successful: Successful responses
            failed: Failed responses

        Returns:
            Weighted blend of responses
        """
        # Define weights for different sources
        weights = {"Claude AI": 0.4, "GitHub Copilot": 0.25, "GitHub": 0.2, "Hugging Face": 0.15}

        blended_parts = []
        sources = []

        for response in successful:
            source = response.get("source", "Unknown")
            content = response.get("content", "")
            weight = weights.get(source, 0.1)

            if content:
                # Add source attribution with weight indicator
                prominence = "●" * int(weight * 10)
                blended_parts.append(f"[{source}] {prominence}\n{content}")
                sources.append(source)

        unified_content = "\n\n" + "─" * 60 + "\n\n".join(blended_parts)

        return {
            "status": "success",
            "unified_content": unified_content,
            "sources": sources,
            "blend_strategy": "weighted",
            "successful_integrations": len(successful),
            "failed_integrations": len(failed),
            "metadata": {"weights": {s: weights.get(s, 0.1) for s in sources}},
        }

    def _concatenate_blend(
        self, successful: List[Dict[str, Any]], failed: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Concatenate all responses sequentially.

        Args:
            successful: Successful responses
            failed: Failed responses

        Returns:
            Concatenated responses
        """
        blended_parts = []
        sources = []

        for response in successful:
            source = response.get("source", "Unknown")
            content = response.get("content", "")

            if content:
                blended_parts.append(f"## {source}\n{content}")
                sources.append(source)

        unified_content = "\n\n".join(blended_parts)

        return {
            "status": "success",
            "unified_content": unified_content,
            "sources": sources,
            "blend_strategy": "concatenate",
            "successful_integrations": len(successful),
            "failed_integrations": len(failed),
        }

    def _prioritize_blend(
        self, successful: List[Dict[str, Any]], failed: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Prioritize responses based on source importance.

        Args:
            successful: Successful responses
            failed: Failed responses

        Returns:
            Prioritized response
        """
        # Priority order
        priority_order = ["Claude AI", "GitHub Copilot", "GitHub", "Hugging Face"]

        # Sort by priority
        sorted_responses = sorted(
            successful,
            key=lambda r: priority_order.index(r.get("source", ""))
            if r.get("source") in priority_order
            else len(priority_order),
        )

        # Primary response is highest priority
        primary = sorted_responses[0] if sorted_responses else {}
        supporting = sorted_responses[1:] if len(sorted_responses) > 1 else []

        primary_content = primary.get("content", "")
        supporting_content = []

        for response in supporting:
            source = response.get("source", "Unknown")
            content = response.get("content", "")
            if content:
                supporting_content.append(f"Additional context from {source}:\n{content}")

        unified_content = primary_content
        if supporting_content:
            unified_content += "\n\n" + "\n\n".join(supporting_content)

        return {
            "status": "success",
            "unified_content": unified_content,
            "primary_source": primary.get("source"),
            "supporting_sources": [r.get("source") for r in supporting],
            "blend_strategy": "prioritize",
            "successful_integrations": len(successful),
            "failed_integrations": len(failed),
        }
