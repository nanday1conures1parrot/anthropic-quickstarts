"""Tests for the Orb core functionality."""

import pytest

from orb_integration.core import InputHandler, Orb, ResponseBlender


class TestInputHandler:
    """Tests for the InputHandler class."""

    def test_condense_input(self):
        """Test input condensation."""
        handler = InputHandler()

        unified = handler.condense_input(
            query="How do I write a Python function?",
            context={"language": "Python"}
        )

        assert "query" in unified
        assert "intent" in unified
        assert "entities" in unified
        assert "context" in unified
        assert unified["query"] == "How do I write a Python function?"
        assert unified["context"]["language"] == "Python"

    def test_extract_intent(self):
        """Test intent extraction."""
        handler = InputHandler()

        # Test code generation intent
        unified = handler.condense_input("Write a function to sort data")
        assert unified["intent"] == "code_generation"

        # Test debugging intent
        unified = handler.condense_input("Debug this error in my application")
        assert unified["intent"] == "debugging"

        # Test explanation intent
        unified = handler.condense_input("What is a lambda function?")
        assert unified["intent"] == "explanation"

    def test_extract_entities(self):
        """Test entity extraction."""
        handler = InputHandler()

        unified = handler.condense_input("Write Python code for GitHub API")

        assert "languages" in unified["entities"]
        assert "technologies" in unified["entities"]
        assert "python" in unified["entities"]["languages"]
        assert "github" in unified["entities"]["technologies"]


class TestResponseBlender:
    """Tests for the ResponseBlender class."""

    def test_blend_empty_responses(self):
        """Test blending with no responses."""
        blender = ResponseBlender()
        result = blender.blend_responses([])

        assert result["status"] == "error"
        assert "No responses" in result["message"]

    def test_blend_successful_responses(self):
        """Test blending successful responses."""
        blender = ResponseBlender()

        responses = [
            {
                "source": "Claude AI",
                "status": "success",
                "content": "Claude's response"
            },
            {
                "source": "GitHub",
                "status": "success",
                "content": "GitHub's response"
            }
        ]

        result = blender.blend_responses(responses, strategy="weighted")

        assert result["status"] == "success"
        assert "unified_content" in result
        assert len(result["sources"]) == 2
        assert result["successful_integrations"] == 2

    def test_blend_with_failures(self):
        """Test blending with some failed responses."""
        blender = ResponseBlender()

        responses = [
            {
                "source": "Claude AI",
                "status": "success",
                "content": "Success"
            },
            {
                "source": "GitHub",
                "status": "error",
                "message": "API error"
            }
        ]

        result = blender.blend_responses(responses)

        assert result["status"] == "success"
        assert result["successful_integrations"] == 1
        assert result["failed_integrations"] == 1

    def test_concatenate_strategy(self):
        """Test concatenate blending strategy."""
        blender = ResponseBlender()

        responses = [
            {"source": "A", "status": "success", "content": "Content A"},
            {"source": "B", "status": "success", "content": "Content B"}
        ]

        result = blender.blend_responses(responses, strategy="concatenate")

        assert result["blend_strategy"] == "concatenate"
        assert "Content A" in result["unified_content"]
        assert "Content B" in result["unified_content"]

    def test_prioritize_strategy(self):
        """Test prioritize blending strategy."""
        blender = ResponseBlender()

        responses = [
            {"source": "GitHub", "status": "success", "content": "GitHub"},
            {"source": "Claude AI", "status": "success", "content": "Claude"}
        ]

        result = blender.blend_responses(responses, strategy="prioritize")

        assert result["blend_strategy"] == "prioritize"
        assert result["primary_source"] == "Claude AI"  # Higher priority


@pytest.mark.asyncio
class TestOrb:
    """Tests for the main Orb orchestrator."""

    async def test_orb_initialization(self):
        """Test Orb initialization."""
        orb = Orb()

        assert len(orb.integrations) == 4  # Claude, GitHub, Copilot, Hugging Face
        assert orb.blend_strategy == "weighted"
        assert orb._execution_count == 0

    async def test_orb_process_query(self):
        """Test query processing through the Orb."""
        orb = Orb()

        response = await orb.process_query("Test query")

        assert "status" in response
        assert "orb_metadata" in response
        assert response["orb_metadata"]["execution_id"] == 1
        assert response["orb_metadata"]["unity_preserved"] is True

    async def test_orb_multiple_executions(self):
        """Test multiple query executions."""
        orb = Orb()

        await orb.process_query("Query 1")
        await orb.process_query("Query 2")
        response = await orb.process_query("Query 3")

        assert orb._execution_count == 3
        assert response["orb_metadata"]["execution_id"] == 3

    async def test_orb_status(self):
        """Test getting Orb status."""
        orb = Orb()

        status = orb.get_status()

        assert "execution_count" in status
        assert "integrations" in status
        assert "blend_strategy" in status
        assert "system_health" in status
        assert len(status["integrations"]) == 4

    async def test_orb_blend_strategy_change(self):
        """Test changing blend strategy."""
        orb = Orb(blend_strategy="weighted")

        orb.set_blend_strategy("concatenate")
        assert orb.blend_strategy == "concatenate"

        orb.set_blend_strategy("prioritize")
        assert orb.blend_strategy == "prioritize"

        with pytest.raises(ValueError):
            orb.set_blend_strategy("invalid")

    async def test_orb_integration_management(self):
        """Test adding and removing integrations."""
        orb = Orb()

        initial_count = len(orb.integrations)

        # Get an integration
        claude = orb.get_integration("Claude AI")
        assert claude is not None
        assert claude.name == "Claude AI"

        # Remove integration
        removed = orb.remove_integration("GitHub")
        assert removed is True
        assert len(orb.integrations) == initial_count - 1

        # Try to remove non-existent integration
        removed = orb.remove_integration("NonExistent")
        assert removed is False
