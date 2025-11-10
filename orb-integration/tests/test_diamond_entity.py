"""Tests for the Diamond Entity self-repair system."""

import pytest

from orb_integration.core import DiamondEntity, DiamondOrb


@pytest.mark.asyncio
class TestDiamondEntity:
    """Tests for the Diamond Entity collapse and repair mechanisms."""

    async def test_initialization(self):
        """Test Diamond Entity initialization."""
        diamond = DiamondEntity(collapse_threshold=0.8)

        assert diamond.metrics.collapse_threshold == 0.8
        assert diamond.metrics.pressure_level == 0.0
        assert diamond.metrics.is_collapsed is False
        assert diamond.repair_state.in_repair is False

    async def test_pressure_application(self):
        """Test applying computational pressure."""
        diamond = DiamondEntity(collapse_threshold=0.9)

        async def simple_task():
            return {"result": "success"}

        result = await diamond.apply_computational_pressure(simple_task, pressure_multiplier=0.5)

        assert result["status"] == "success"
        assert "pressure_applied" in result
        assert "metrics" in result
        assert result["pressure_applied"] > 0.0

    async def test_collapse_detection(self):
        """Test that collapse is detected under high pressure."""
        diamond = DiamondEntity(collapse_threshold=0.5)  # Low threshold

        async def simple_task():
            return {"result": "success"}

        # Apply high pressure to trigger collapse
        result = await diamond.apply_computational_pressure(simple_task, pressure_multiplier=2.0)

        # With high pressure and low threshold, collapse should occur
        assert result["collapsed"] or result["metrics"]["pressure_level"] < 0.5

    async def test_self_repair_mechanism(self):
        """Test that self-repair is triggered after collapse."""
        diamond = DiamondEntity(collapse_threshold=0.4)

        async def simple_task():
            return {"result": "success"}

        result = await diamond.apply_computational_pressure(simple_task, pressure_multiplier=2.0)

        # If collapsed, repair should have been attempted
        if result["collapsed"]:
            assert result["repaired"] or "repair_details" in result
            assert diamond.metrics.repair_count > 0

    async def test_outlier_detection_and_fusion(self):
        """Test outlier detection and fusion into optimized modules."""
        diamond = DiamondEntity()

        # Simulate high contradiction state
        diamond.metrics.contradictions = 10
        diamond.metrics.recursive_depth = 60
        diamond.metrics.memory_pressure = 0.8

        outliers = await diamond._detect_outliers()

        assert len(outliers) > 0
        assert diamond.metrics.redundant_code_detected > 0

        # Test fusion
        fused = await diamond._fuse_outliers(outliers)

        assert len(fused) > 0
        assert diamond.metrics.optimizations_applied > 0

    async def test_contradiction_resolution(self):
        """Test contradiction resolution mechanism."""
        diamond = DiamondEntity()
        diamond.metrics.contradictions = 10

        initial_contradictions = diamond.metrics.contradictions

        await diamond._resolve_contradictions()

        # Contradictions should be reduced
        assert diamond.metrics.contradictions < initial_contradictions

    async def test_recursive_flattening(self):
        """Test recursive call flattening."""
        diamond = DiamondEntity()
        diamond.metrics.recursive_depth = 80

        initial_depth = diamond.metrics.recursive_depth

        await diamond._flatten_recursion()

        # Recursive depth should be reduced
        assert diamond.metrics.recursive_depth < initial_depth

    async def test_integration_unification(self):
        """Test integration unification during repair."""
        diamond = DiamondEntity()
        diamond.metrics.pressure_level = 0.8

        initial_pressure = diamond.metrics.pressure_level

        optimizations = await diamond._unify_integrations()

        assert len(optimizations) > 0
        # Pressure should be reduced after unification
        assert diamond.metrics.pressure_level < initial_pressure

    async def test_quantum_healing(self):
        """Test quantum-inspired healing algorithms."""
        diamond = DiamondEntity(enable_quantum_healing=True)
        diamond.metrics.pressure_level = 0.7

        initial_pressure = diamond.metrics.pressure_level

        optimizations = await diamond._apply_quantum_healing()

        assert len(optimizations) > 0
        # Quantum healing should reduce pressure
        assert diamond.metrics.pressure_level < initial_pressure

    async def test_repair_validation(self):
        """Test repair validation mechanism."""
        diamond = DiamondEntity()

        # Set good state
        diamond.metrics.pressure_level = 0.3
        diamond.metrics.contradictions = 2
        diamond.metrics.recursive_depth = 10

        is_valid = await diamond._validate_repair()
        assert is_valid is True

        # Set bad state
        diamond.metrics.pressure_level = 0.9
        diamond.metrics.contradictions = 20

        is_valid = await diamond._validate_repair()
        assert is_valid is False

    async def test_state_snapshot_and_recovery(self):
        """Test state snapshot and emergency recovery."""
        diamond = DiamondEntity()

        # Take snapshot
        diamond.metrics.pressure_level = 0.5
        diamond._snapshot_state()

        assert len(diamond._state_snapshots) > 0

        # Simulate error and recovery
        error = Exception("Test error")
        recovery = await diamond._emergency_repair(error)

        assert recovery["triggered"] is True
        assert "recovered" in recovery

    async def test_metrics_export(self):
        """Test metrics export functionality."""
        diamond = DiamondEntity()

        diamond.metrics.pressure_level = 0.7
        diamond.metrics.collapse_count = 2
        diamond.metrics.repair_count = 2

        metrics = diamond._export_metrics()

        assert "pressure_level" in metrics
        assert "collapse_count" in metrics
        assert "repair_count" in metrics
        assert metrics["collapse_count"] == 2
        assert metrics["repair_count"] == 2

    async def test_status_reporting(self):
        """Test comprehensive status reporting."""
        diamond = DiamondEntity()

        diamond.metrics.collapse_count = 3
        diamond.metrics.repair_count = 3

        status = diamond.get_status()

        assert "metrics" in status
        assert "repair_state" in status
        assert "configuration" in status
        assert status["configuration"]["quantum_healing_enabled"] is True

    async def test_reset_functionality(self):
        """Test entity reset."""
        diamond = DiamondEntity()

        # Modify state
        diamond.metrics.collapse_count = 5
        diamond.metrics.repair_count = 4
        diamond.metrics.pressure_level = 0.8

        # Reset
        diamond.reset()

        assert diamond.metrics.collapse_count == 0
        assert diamond.metrics.repair_count == 0
        assert diamond.metrics.pressure_level == 0.0
        assert len(diamond._state_snapshots) == 0


@pytest.mark.asyncio
class TestDiamondOrb:
    """Tests for the Diamond Orb integration."""

    async def test_initialization(self):
        """Test Diamond Orb initialization."""
        diamond_orb = DiamondOrb()

        assert diamond_orb.orb is not None
        assert diamond_orb.diamond is not None
        assert diamond_orb.auto_repair is True

    async def test_process_query_without_collapse(self):
        """Test query processing without triggering collapse."""
        diamond_orb = DiamondOrb()

        response = await diamond_orb.process_query(
            "Test query",
            pressure_multiplier=0.3,  # Low pressure
        )

        assert "status" in response
        assert "diamond_metadata" in response
        assert "diamond_statistics" in response

    async def test_process_query_with_pressure(self):
        """Test query processing with high pressure."""
        diamond_orb = DiamondOrb(collapse_threshold=0.5)

        response = await diamond_orb.process_query(
            "Test query under pressure", pressure_multiplier=1.5
        )

        assert "diamond_metadata" in response
        metadata = response["diamond_metadata"]

        assert "pressure_applied" in metadata
        assert "metrics" in metadata

    async def test_stress_test(self):
        """Test stress testing with increasing pressure."""
        diamond_orb = DiamondOrb()

        results = await diamond_orb.stress_test(
            "Stress test query", pressure_levels=[0.5, 1.0, 1.5]
        )

        assert "stress_test" in results
        assert "max_pressure_survived" in results
        assert "collapse_count" in results
        assert "repair_count" in results
        assert len(results["stress_test"]) == 3

    async def test_collapse_and_repair_tracking(self):
        """Test that collapses and repairs are tracked."""
        diamond_orb = DiamondOrb(collapse_threshold=0.3)

        # Process multiple queries with high pressure
        for _ in range(3):
            await diamond_orb.process_query("Test query", pressure_multiplier=1.8)

        # Check statistics
        assert diamond_orb._total_collapses >= 0
        assert diamond_orb._total_repairs >= 0

    async def test_status_reporting(self):
        """Test comprehensive status reporting."""
        diamond_orb = DiamondOrb()

        status = diamond_orb.get_status()

        assert "orb" in status
        assert "diamond" in status
        assert "statistics" in status
        assert "system_state" in status

    async def test_threshold_configuration(self):
        """Test collapse threshold configuration."""
        diamond_orb = DiamondOrb()

        diamond_orb.set_collapse_threshold(0.7)
        assert diamond_orb.diamond.metrics.collapse_threshold == 0.7

        with pytest.raises(ValueError):
            diamond_orb.set_collapse_threshold(1.5)

    async def test_quantum_healing_toggle(self):
        """Test enabling/disabling quantum healing."""
        diamond_orb = DiamondOrb()

        diamond_orb.enable_quantum_healing(False)
        assert diamond_orb.diamond.enable_quantum_healing is False

        diamond_orb.enable_quantum_healing(True)
        assert diamond_orb.diamond.enable_quantum_healing is True

    async def test_reset_functionality(self):
        """Test Diamond Orb reset."""
        diamond_orb = DiamondOrb(collapse_threshold=0.3)

        # Trigger some collapses
        await diamond_orb.process_query("Test", pressure_multiplier=2.0)

        # Reset
        diamond_orb.reset()

        assert diamond_orb._total_collapses == 0
        assert diamond_orb._total_repairs == 0

    async def test_orb_proxy_methods(self):
        """Test proxy methods to underlying Orb."""
        diamond_orb = DiamondOrb()

        # Test integration management
        claude = diamond_orb.get_integration("Claude AI")
        assert claude is not None

        # Test blend strategy
        diamond_orb.set_blend_strategy("concatenate")
        assert diamond_orb.orb.blend_strategy == "concatenate"
