"""Main Orb orchestrator that unifies all integrations."""

import asyncio
from typing import Dict, Any, List, Optional
from ..integrations import (
    BaseIntegration,
    ClaudeIntegration,
    GitHubIntegration,
    CopilotIntegration,
    HuggingFaceIntegration
)
from .input_handler import InputHandler
from .response_blender import ResponseBlender


class Orb:
    """
    The Orb: A unified AI integration system.
    
    The Orb represents a single, indivisible system that blends multiple AI
    technologies into one cohesive entity. It processes all inputs through
    every integrated system simultaneously and produces unified responses
    that draw from the collective intelligence of all components.
    """
    
    def __init__(
        self,
        anthropic_api_key: Optional[str] = None,
        blend_strategy: str = "weighted"
    ):
        """
        Initialize the Orb system.
        
        Args:
            anthropic_api_key: API key for Claude integration
            blend_strategy: Strategy for blending responses ("weighted", "concatenate", "prioritize")
        """
        # Core components
        self.input_handler = InputHandler()
        self.response_blender = ResponseBlender()
        self.blend_strategy = blend_strategy
        
        # Initialize all integrations
        self.integrations: List[BaseIntegration] = [
            ClaudeIntegration(api_key=anthropic_api_key),
            GitHubIntegration(),
            CopilotIntegration(),
            HuggingFaceIntegration()
        ]
        
        # State tracking
        self._execution_count = 0
        self._unified_state: Dict[str, Any] = {}
    
    async def process_query(
        self,
        query: str,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Process a user query through the entire Orb system.
        
        This method represents the core "orbital execution flow" where the query
        is simultaneously processed by all integrations and the results are
        blended into a unified response.
        
        Args:
            query: User's input query
            context: Optional contextual information
            
        Returns:
            Unified response from all integrations
        """
        # Increment execution counter
        self._execution_count += 1
        
        # Phase 1: Condense input through central handler
        unified_input = self.input_handler.condense_input(
            query=query,
            context=context,
            metadata={"execution_id": self._execution_count}
        )
        
        # Phase 2: Spin up the Orb singularity - process through all integrations simultaneously
        responses = await self._execute_orbital_flow(unified_input)
        
        # Phase 3: Blend responses into unified output
        unified_response = self.response_blender.blend_responses(
            responses=responses,
            strategy=self.blend_strategy
        )
        
        # Phase 4: Update unified state (self-compression)
        self._update_unified_state(unified_input, unified_response)
        
        # Add Orb metadata
        unified_response["orb_metadata"] = {
            "execution_id": self._execution_count,
            "integrations_engaged": len(self.integrations),
            "active_integrations": len([i for i in self.integrations if i.is_enabled()]),
            "blend_strategy": self.blend_strategy,
            "unity_preserved": True
        }
        
        return unified_response
    
    async def _execute_orbital_flow(
        self,
        unified_input: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """
        Execute the orbital flow - process input through all integrations simultaneously.
        
        This represents the core principle of the Orb: all integrations operate
        as one inseparable system, processing the input in parallel.
        
        Args:
            unified_input: Condensed input from the input handler
            
        Returns:
            List of responses from all integrations
        """
        # Create tasks for all enabled integrations
        tasks = []
        for integration in self.integrations:
            if integration.is_enabled():
                tasks.append(integration.process(unified_input))
        
        # Execute all integrations simultaneously (the Orb singularity)
        if tasks:
            responses = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Convert exceptions to error responses
            processed_responses = []
            for i, response in enumerate(responses):
                if isinstance(response, Exception):
                    processed_responses.append({
                        "source": self.integrations[i].name,
                        "status": "error",
                        "message": str(response),
                        "content": None
                    })
                else:
                    processed_responses.append(response)
            
            return processed_responses
        else:
            return []
    
    def _update_unified_state(
        self,
        unified_input: Dict[str, Any],
        unified_response: Dict[str, Any]
    ) -> None:
        """
        Update the Orb's unified state (perpetual self-compression).
        
        Args:
            unified_input: The processed input
            unified_response: The unified response
        """
        execution_id = self._execution_count
        
        self._unified_state[f"execution_{execution_id}"] = {
            "input": unified_input,
            "response": unified_response,
            "timestamp": unified_input.get("timestamp")
        }
        
        # Maintain only recent history to prevent unbounded growth
        if len(self._unified_state) > 100:
            oldest_key = min(self._unified_state.keys())
            del self._unified_state[oldest_key]
    
    def get_integration(self, name: str) -> Optional[BaseIntegration]:
        """
        Get an integration by name.
        
        Args:
            name: Name of the integration
            
        Returns:
            The integration if found, None otherwise
        """
        for integration in self.integrations:
            if integration.name == name:
                return integration
        return None
    
    def add_integration(self, integration: BaseIntegration) -> None:
        """
        Add a new integration to the Orb.
        
        Args:
            integration: The integration to add
        """
        self.integrations.append(integration)
    
    def remove_integration(self, name: str) -> bool:
        """
        Remove an integration from the Orb.
        
        Args:
            name: Name of the integration to remove
            
        Returns:
            True if removed, False if not found
        """
        for i, integration in enumerate(self.integrations):
            if integration.name == name:
                self.integrations.pop(i)
                return True
        return False
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get the current status of the Orb system.
        
        Returns:
            Status dictionary with system information
        """
        return {
            "execution_count": self._execution_count,
            "integrations": [
                {
                    "name": i.name,
                    "enabled": i.is_enabled(),
                    "type": type(i).__name__
                }
                for i in self.integrations
            ],
            "blend_strategy": self.blend_strategy,
            "state_size": len(self._unified_state),
            "system_health": "operational"
        }
    
    def set_blend_strategy(self, strategy: str) -> None:
        """
        Set the response blending strategy.
        
        Args:
            strategy: Blending strategy ("weighted", "concatenate", "prioritize")
        """
        valid_strategies = ["weighted", "concatenate", "prioritize"]
        if strategy in valid_strategies:
            self.blend_strategy = strategy
        else:
            raise ValueError(f"Invalid strategy. Must be one of: {valid_strategies}")
