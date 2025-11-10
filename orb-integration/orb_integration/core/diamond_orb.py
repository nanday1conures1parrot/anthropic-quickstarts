"""
Diamond Orb: Integration of Diamond Entity with the Orb system.

This module combines the unified Orb system with the Diamond Entity's
self-repair capabilities, creating a resilient AI integration system
that can withstand and recover from extreme computational pressure.
"""

from typing import Any, Dict, Optional

from .diamond_entity import DiamondEntity
from .orb import Orb


class DiamondOrb:
    """
    The Diamond Orb - A self-healing unified AI integration system.

    This class wraps the Orb system with Diamond Entity capabilities,
    providing automatic collapse detection and self-repair for robust
    operation under extreme conditions.

    The Diamond Orb embodies the concept of pressure-induced unification:
    when stressed, it collapses into a simpler form, then reconstructs
    itself into an optimized, crystalline structure - like carbon forming
    a diamond.
    """

    def __init__(
        self,
        anthropic_api_key: Optional[str] = None,
        blend_strategy: str = "weighted",
        collapse_threshold: float = 0.85,
        enable_quantum_healing: bool = True,
        auto_repair: bool = True,
    ):
        """
        Initialize the Diamond Orb.

        Args:
            anthropic_api_key: API key for Claude integration
            blend_strategy: Strategy for blending responses
            collapse_threshold: Pressure threshold for triggering collapse
            enable_quantum_healing: Enable quantum-inspired healing algorithms
            auto_repair: Automatically repair on collapse detection
        """
        # Initialize core Orb
        self.orb = Orb(anthropic_api_key=anthropic_api_key, blend_strategy=blend_strategy)

        # Initialize Diamond Entity
        self.diamond = DiamondEntity(
            collapse_threshold=collapse_threshold, enable_quantum_healing=enable_quantum_healing
        )

        self.auto_repair = auto_repair
        self._total_collapses = 0
        self._total_repairs = 0

    async def process_query(
        self, query: str, context: Optional[Dict[str, Any]] = None, pressure_multiplier: float = 1.0
    ) -> Dict[str, Any]:
        """
        Process a query through the Diamond Orb with pressure resistance.

        This method processes queries through the unified Orb system while
        monitoring for collapse conditions. If collapse is detected, the
        system automatically initiates self-repair procedures.

        Args:
            query: User's input query
            context: Optional contextual information
            pressure_multiplier: Multiplier for computational pressure (0-2)

        Returns:
            Unified response with diamond entity metadata
        """
        # Execute query through diamond entity with pressure monitoring
        result = await self.diamond.apply_computational_pressure(
            self.orb.process_query, query, context, pressure_multiplier=pressure_multiplier
        )

        # Track collapse statistics
        if result.get("collapsed"):
            self._total_collapses += 1

        if result.get("repaired"):
            self._total_repairs += 1

        # Prepare response
        response = result.get("data", {})

        # Add diamond entity metadata
        if isinstance(response, dict):
            response["diamond_metadata"] = {
                "collapsed": result.get("collapsed", False),
                "repaired": result.get("repaired", False),
                "pressure_applied": result.get("pressure_applied", 0.0),
                "execution_time": result.get("execution_time", 0.0),
                "metrics": result.get("metrics", {}),
                "repair_details": result.get("repair_details", {}),
            }

            # Add cumulative statistics
            response["diamond_statistics"] = {
                "total_collapses": self._total_collapses,
                "total_repairs": self._total_repairs,
                "repair_success_rate": (
                    self._total_repairs / self._total_collapses
                    if self._total_collapses > 0
                    else 1.0
                ),
            }

        return response

    async def stress_test(
        self, query: str, pressure_levels: Optional[list] = None
    ) -> Dict[str, Any]:
        """
        Perform stress test with increasing pressure levels.

        Args:
            query: Query to test with
            pressure_levels: List of pressure multipliers to test

        Returns:
            Stress test results
        """
        if pressure_levels is None:
            pressure_levels = [0.5, 1.0, 1.5, 2.0]

        results = []

        for pressure in pressure_levels:
            result = await self.process_query(query=query, pressure_multiplier=pressure)

            results.append(
                {
                    "pressure_level": pressure,
                    "collapsed": result.get("diamond_metadata", {}).get("collapsed", False),
                    "repaired": result.get("diamond_metadata", {}).get("repaired", False),
                    "execution_time": result.get("diamond_metadata", {}).get("execution_time", 0.0),
                    "health_score": result.get("diamond_metadata", {})
                    .get("metrics", {})
                    .get("health_score", 0.0),
                }
            )

        return {
            "stress_test": results,
            "max_pressure_survived": max(
                r["pressure_level"] for r in results if not r["collapsed"] or r["repaired"]
            ),
            "collapse_count": sum(1 for r in results if r["collapsed"]),
            "repair_count": sum(1 for r in results if r["repaired"]),
        }

    def get_status(self) -> Dict[str, Any]:
        """Get comprehensive status of the Diamond Orb system."""
        orb_status = self.orb.get_status()
        diamond_status = self.diamond.get_status()

        return {
            "orb": orb_status,
            "diamond": diamond_status,
            "statistics": {
                "total_collapses": self._total_collapses,
                "total_repairs": self._total_repairs,
                "repair_success_rate": (
                    self._total_repairs / self._total_collapses
                    if self._total_collapses > 0
                    else 1.0
                ),
                "auto_repair_enabled": self.auto_repair,
            },
            "system_state": "collapsed"
            if diamond_status["metrics"]["is_collapsed"]
            else "repairing"
            if diamond_status["repair_state"]["in_repair"]
            else "operational",
        }

    def set_collapse_threshold(self, threshold: float) -> None:
        """
        Set the collapse threshold.

        Args:
            threshold: Threshold value between 0.0 and 1.0
        """
        if 0.0 <= threshold <= 1.0:
            self.diamond.metrics.collapse_threshold = threshold
        else:
            raise ValueError("Threshold must be between 0.0 and 1.0")

    def enable_quantum_healing(self, enable: bool = True) -> None:
        """
        Enable or disable quantum healing algorithms.

        Args:
            enable: Whether to enable quantum healing
        """
        self.diamond.enable_quantum_healing = enable

    def reset(self) -> None:
        """Reset the Diamond Orb to initial state."""
        self.diamond.reset()
        self._total_collapses = 0
        self._total_repairs = 0

    # Proxy methods to underlying Orb
    def get_integration(self, name: str):
        """Get an integration by name from the underlying Orb."""
        return self.orb.get_integration(name)

    def add_integration(self, integration):
        """Add an integration to the underlying Orb."""
        return self.orb.add_integration(integration)

    def remove_integration(self, name: str):
        """Remove an integration from the underlying Orb."""
        return self.orb.remove_integration(name)

    def set_blend_strategy(self, strategy: str):
        """Set the response blending strategy."""
        return self.orb.set_blend_strategy(strategy)
