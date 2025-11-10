"""Input handler for the Orb system."""

from typing import Dict, Any, List, Optional
import re


class InputHandler:
    """
    Central input handler that condenses user inputs for the Orb system.
    
    This component transforms various input formats into a unified representation
    that can be processed by all integrated systems simultaneously.
    """
    
    def __init__(self):
        """Initialize the input handler."""
        self._history: List[Dict[str, Any]] = []
    
    def condense_input(
        self,
        query: str,
        context: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Condense user input into a unified format for the Orb.
        
        Args:
            query: The user's input query
            context: Optional contextual information
            metadata: Optional metadata about the input
            
        Returns:
            Unified input dictionary that all integrations can process
        """
        # Extract intent and key information
        intent = self._extract_intent(query)
        entities = self._extract_entities(query)
        
        # Build unified input
        unified_input = {
            "query": query,
            "intent": intent,
            "entities": entities,
            "context": context or {},
            "metadata": metadata or {},
            "timestamp": self._get_timestamp()
        }
        
        # Add to history
        self._history.append(unified_input)
        
        return unified_input
    
    def _extract_intent(self, query: str) -> str:
        """
        Extract the primary intent from the query.
        
        Args:
            query: User's input query
            
        Returns:
            Identified intent category
        """
        query_lower = query.lower()
        
        # Simple intent classification based on keywords
        if any(word in query_lower for word in ["write", "create", "implement", "code"]):
            return "code_generation"
        elif any(word in query_lower for word in ["debug", "fix", "error", "bug"]):
            return "debugging"
        elif any(word in query_lower for word in ["explain", "what", "how", "why"]):
            return "explanation"
        elif any(word in query_lower for word in ["optimize", "improve", "refactor"]):
            return "optimization"
        elif any(word in query_lower for word in ["search", "find", "locate"]):
            return "search"
        else:
            return "general"
    
    def _extract_entities(self, query: str) -> Dict[str, List[str]]:
        """
        Extract key entities from the query.
        
        Args:
            query: User's input query
            
        Returns:
            Dictionary of entity types and their values
        """
        entities = {
            "languages": [],
            "technologies": [],
            "concepts": []
        }
        
        # Programming languages
        languages = ["python", "javascript", "typescript", "java", "c++", "go", "rust"]
        for lang in languages:
            if lang in query.lower():
                entities["languages"].append(lang)
        
        # Technologies
        technologies = ["github", "git", "api", "database", "web", "mobile", "cloud"]
        for tech in technologies:
            if tech in query.lower():
                entities["technologies"].append(tech)
        
        # Extract potential concept words (capitalized words)
        concepts = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', query)
        entities["concepts"] = concepts
        
        return entities
    
    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        from datetime import datetime
        return datetime.utcnow().isoformat()
    
    def get_history(self) -> List[Dict[str, Any]]:
        """Get input history."""
        return self._history.copy()
    
    def clear_history(self) -> None:
        """Clear input history."""
        self._history.clear()
