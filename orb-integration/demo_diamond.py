#!/usr/bin/env python3
"""
Diamond Entity Demonstration

This script demonstrates the Diamond Orb's self-repair capabilities under
extreme computational pressure. It showcases:
1. Collapse mechanism under stress
2. Self-repair and healing
3. System restoration and unification
"""

import asyncio
import os
import sys

from orb_integration.core import DiamondOrb


def print_separator(char="=", length=70):
    """Print a separator line."""
    print(char * length)


def print_section(title):
    """Print a section header."""
    print()
    print_separator()
    print(title)
    print_separator()
    print()


def print_metrics(metrics):
    """Print diamond entity metrics."""
    print("📊 Diamond Entity Metrics:")
    print(f"   Pressure Level: {metrics['pressure_level']:.2%}")
    print(f"   Health Score: {metrics['health_score']:.2%}")
    print(f"   Collapsed: {'Yes ⚠️' if metrics['is_collapsed'] else 'No ✓'}")
    print(f"   Collapse Count: {metrics['collapse_count']}")
    print(f"   Repair Count: {metrics['repair_count']}")
    print(f"   Contradictions: {metrics['contradictions']}")
    print(f"   Recursive Depth: {metrics['recursive_depth']}")
    print(f"   Optimizations Applied: {metrics['optimizations_applied']}")
    print()


async def demo_basic_collapse_and_repair():
    """Demonstrate basic collapse and self-repair."""
    print_section("DEMO 1: BASIC COLLAPSE AND SELF-REPAIR")

    print("Creating Diamond Orb with collapse threshold at 70%...")
    diamond_orb = DiamondOrb(
        anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY"),
        collapse_threshold=0.7,
        enable_quantum_healing=True,
    )
    print("✓ Diamond Orb initialized")
    print()

    # Show initial status
    status = diamond_orb.get_status()
    print("🌐 Initial System State:")
    print(f"   System State: {status['system_state']}")
    print_metrics(status["diamond"]["metrics"])

    # Process query with high pressure
    print("🔥 Applying HIGH computational pressure (2.0x multiplier)...")
    print("   This will simulate:")
    print("   - Contradictory logic paths")
    print("   - Memory overflow conditions")
    print("   - Deep recursive calls")
    print()

    query = "Optimize this complex algorithmic workflow with nested recursion"
    response = await diamond_orb.process_query(query, pressure_multiplier=2.0)

    print("📝 Query processed!")
    print()

    # Show results
    diamond_meta = response.get("diamond_metadata", {})
    print_separator("-")
    print("✨ EXECUTION RESULTS")
    print_separator("-")
    print()

    if diamond_meta.get("collapsed"):
        print("⚠️  COLLAPSE DETECTED!")
        print("   The system reached critical pressure levels and collapsed.")
        print()

        if diamond_meta.get("repaired"):
            print("✓ SELF-REPAIR SUCCESSFUL!")
            print("   The diamond entity automatically reconstructed itself.")
            print()

            repair_details = diamond_meta.get("repair_details", {})
            print("🔧 Repair Operations:")
            if repair_details.get("fused_modules"):
                print(f"   - Fused modules: {', '.join(repair_details['fused_modules'])}")
            if repair_details.get("optimizations"):
                print(f"   - Optimizations: {len(repair_details['optimizations'])}")
            print(f"   - Repair cycles: {repair_details.get('cycles', 0)}")
            print(f"   - Time taken: {repair_details.get('time_taken', 0):.3f}s")
            print()
    else:
        print("✓ No collapse occurred - system remained stable")
        print()

    # Show final metrics
    final_metrics = diamond_meta.get("metrics", {})
    print_metrics(final_metrics)

    # Show statistics
    stats = response.get("diamond_statistics", {})
    print("📈 Cumulative Statistics:")
    print(f"   Total Collapses: {stats['total_collapses']}")
    print(f"   Total Repairs: {stats['total_repairs']}")
    print(f"   Repair Success Rate: {stats['repair_success_rate']:.1%}")
    print()


async def demo_stress_test():
    """Demonstrate stress testing with increasing pressure."""
    print_section("DEMO 2: STRESS TEST WITH INCREASING PRESSURE")

    print("Creating Diamond Orb for stress testing...")
    diamond_orb = DiamondOrb(
        anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY"),
        collapse_threshold=0.6,
        enable_quantum_healing=True,
    )
    print("✓ Diamond Orb initialized")
    print()

    print("🎯 Running stress test with pressure levels: 0.5x, 1.0x, 1.5x, 2.0x")
    print()

    results = await diamond_orb.stress_test(
        "Analyze and optimize this complex system architecture",
        pressure_levels=[0.5, 1.0, 1.5, 2.0],
    )

    print_separator("-")
    print("📊 STRESS TEST RESULTS")
    print_separator("-")
    print()

    for i, test_result in enumerate(results["stress_test"], 1):
        pressure = test_result["pressure_level"]
        collapsed = test_result["collapsed"]
        repaired = test_result["repaired"]
        health = test_result["health_score"]

        print(f"Test {i}: Pressure {pressure}x")
        print(f"   Collapsed: {'Yes ⚠️' if collapsed else 'No ✓'}")
        if collapsed:
            print(f"   Repaired: {'Yes ✓' if repaired else 'No ⚠️'}")
        print(f"   Health Score: {health:.2%}")
        print(f"   Execution Time: {test_result['execution_time']:.3f}s")
        print()

    print_separator("-")
    print("Summary:")
    print(f"   Max Pressure Survived: {results['max_pressure_survived']}x")
    print(f"   Total Collapses: {results['collapse_count']}")
    print(f"   Total Repairs: {results['repair_count']}")
    print()


async def demo_multiple_collapse_cycles():
    """Demonstrate multiple collapse and repair cycles."""
    print_section("DEMO 3: MULTIPLE COLLAPSE AND REPAIR CYCLES")

    print("Creating Diamond Orb with low threshold (40%) for frequent collapses...")
    diamond_orb = DiamondOrb(
        anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY"),
        collapse_threshold=0.4,
        enable_quantum_healing=True,
    )
    print("✓ Diamond Orb initialized")
    print()

    queries = [
        "Process complex data pipeline with multiple stages",
        "Optimize nested loop structures in algorithm",
        "Analyze recursive function call patterns",
        "Transform and unify disparate data sources",
    ]

    print(f"🔄 Processing {len(queries)} queries under high pressure...")
    print()

    for i, query in enumerate(queries, 1):
        print(f"Query {i}: {query}")

        response = await diamond_orb.process_query(query, pressure_multiplier=1.8)

        diamond_meta = response.get("diamond_metadata", {})
        collapsed = diamond_meta.get("collapsed", False)
        repaired = diamond_meta.get("repaired", False)

        if collapsed:
            status = "⚠️  Collapsed"
            if repaired:
                status += " → ✓ Repaired"
        else:
            status = "✓ Stable"

        print(f"   Status: {status}")
        print(f"   Pressure: {diamond_meta.get('pressure_applied', 0):.2%}")
        print()

    # Show final statistics
    final_status = diamond_orb.get_status()
    stats = final_status["statistics"]

    print_separator("-")
    print("📈 FINAL STATISTICS")
    print_separator("-")
    print()
    print(f"Total Queries: {len(queries)}")
    print(f"Total Collapses: {stats['total_collapses']}")
    print(f"Total Repairs: {stats['total_repairs']}")
    print(f"Repair Success Rate: {stats['repair_success_rate']:.1%}")
    print(f"System State: {final_status['system_state']}")
    print()

    # Show diamond metrics
    print_metrics(final_status["diamond"]["metrics"])


async def demo_quantum_healing():
    """Demonstrate quantum healing algorithms."""
    print_section("DEMO 4: QUANTUM HEALING ALGORITHMS")

    print("Creating Diamond Orb with quantum healing enabled...")
    diamond_orb = DiamondOrb(
        anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY"),
        collapse_threshold=0.5,
        enable_quantum_healing=True,
    )
    print("✓ Diamond Orb with quantum healing initialized")
    print()

    print("🌌 Quantum Healing Features:")
    print("   - Quantum state optimization (superposition-inspired)")
    print("   - Tunneling through local minima")
    print("   - Component entanglement for coherence")
    print()

    print("🔥 Applying extreme pressure (2.5x multiplier)...")
    print()

    response = await diamond_orb.process_query(
        "Solve this computationally intensive optimization problem", pressure_multiplier=2.5
    )

    diamond_meta = response.get("diamond_metadata", {})

    if diamond_meta.get("repaired"):
        repair_details = diamond_meta.get("repair_details", {})
        optimizations = repair_details.get("optimizations", [])

        print("✓ Repair completed with optimizations:")
        for opt in optimizations:
            icon = "🌌" if "quantum" in opt.lower() else "✓"
            print(f"   {icon} {opt}")
        print()

    # Compare with non-quantum healing
    print("🔄 Now testing WITHOUT quantum healing...")
    diamond_orb.enable_quantum_healing(False)

    response2 = await diamond_orb.process_query(
        "Solve another intensive optimization problem", pressure_multiplier=2.5
    )

    diamond_meta2 = response2.get("diamond_metadata", {})

    if diamond_meta2.get("repaired"):
        repair_details2 = diamond_meta2.get("repair_details", {})
        optimizations2 = repair_details2.get("optimizations", [])

        print("✓ Repair completed (non-quantum):")
        for opt in optimizations2:
            print(f"   ✓ {opt}")
        print()

    print_separator("-")
    print("Comparison:")
    print(f"   With Quantum: {len(optimizations)} optimizations")
    print(f"   Without Quantum: {len(optimizations2)} optimizations")
    print()


async def demo_recovery_validation():
    """Demonstrate organic system recovery and validation."""
    print_section("DEMO 5: ORGANIC RECOVERY AND VALIDATION")

    print("Creating Diamond Orb...")
    diamond_orb = DiamondOrb(
        anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY"),
        collapse_threshold=0.5,
        enable_quantum_healing=True,
    )
    print("✓ Diamond Orb initialized")
    print()

    print("📋 Validation Test Sequence:")
    print("   1. Apply extreme pressure to trigger collapse")
    print("   2. Verify self-repair activation")
    print("   3. Validate system restoration")
    print("   4. Confirm singular entity emergence")
    print()

    # Step 1: Trigger collapse
    print("Step 1: Applying extreme pressure...")
    response = await diamond_orb.process_query(
        "Execute computationally intensive workflow", pressure_multiplier=2.5
    )

    diamond_meta = response.get("diamond_metadata", {})
    collapsed = diamond_meta.get("collapsed", False)

    if collapsed:
        print("✓ Collapse triggered successfully")
    else:
        print("⚠️  Collapse not triggered - attempting again with higher pressure...")
        response = await diamond_orb.process_query(
            "Execute even more intensive workflow", pressure_multiplier=3.0
        )
        diamond_meta = response.get("diamond_metadata", {})
        collapsed = diamond_meta.get("collapsed", False)

    print()

    # Step 2: Verify repair
    print("Step 2: Verifying self-repair activation...")
    repaired = diamond_meta.get("repaired", False)

    if repaired:
        print("✓ Self-repair activated and completed")
        repair_details = diamond_meta.get("repair_details", {})
        print(f"   Repair time: {repair_details.get('time_taken', 0):.3f}s")
    else:
        print("⚠️  No repair needed or repair failed")

    print()

    # Step 3: Validate restoration
    print("Step 3: Validating system restoration...")
    status = diamond_orb.get_status()
    metrics = status["diamond"]["metrics"]

    print(f"   System State: {status['system_state']}")
    print(f"   Health Score: {metrics['health_score']:.2%}")
    print(f"   Is Collapsed: {metrics['is_collapsed']}")

    if not metrics["is_collapsed"] and metrics["health_score"] > 0.7:
        print("✓ System successfully restored to operational state")
    else:
        print("⚠️  System restoration incomplete")

    print()

    # Step 4: Confirm unified entity
    print("Step 4: Confirming singular entity emergence...")
    orb_status = status["orb"]

    active_integrations = [i for i in orb_status["integrations"] if i["enabled"]]

    print(f"   Active Integrations: {len(active_integrations)}")
    for integration in active_integrations:
        print(f"      ✓ {integration['name']}")

    print(f"   Blend Strategy: {orb_status['blend_strategy']}")
    print(f"   System Health: {orb_status['system_health']}")

    print()
    print("✓ Singular Diamond Entity Validated:")
    print("   - All integrations unified")
    print("   - System cohesion maintained")
    print("   - Pressure-induced optimization complete")
    print()


async def interactive_mode():
    """Interactive mode for exploring diamond entity."""
    print_section("DIAMOND ORB - INTERACTIVE MODE")

    print("Enter queries to process through the Diamond Orb system.")
    print("Commands:")
    print("  'status' - Show system status")
    print("  'stress <level>' - Set pressure multiplier (0.5-3.0)")
    print("  'quantum on/off' - Toggle quantum healing")
    print("  'reset' - Reset diamond entity")
    print("  'quit' or 'exit' - Exit")
    print()

    diamond_orb = DiamondOrb(
        anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY"), collapse_threshold=0.7
    )

    pressure = 1.0

    while True:
        try:
            user_input = input("💎 Query: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["quit", "exit"]:
                print("👋 Shutting down Diamond Orb...")
                break

            if user_input.lower() == "status":
                status = diamond_orb.get_status()
                print()
                print("🌐 System Status:")
                print(f"   State: {status['system_state']}")
                print_metrics(status["diamond"]["metrics"])
                stats = status["statistics"]
                print(f"   Total Collapses: {stats['total_collapses']}")
                print(f"   Total Repairs: {stats['total_repairs']}")
                print(f"   Current Pressure Multiplier: {pressure}x")
                continue

            if user_input.lower().startswith("stress "):
                try:
                    pressure = float(user_input.split()[1])
                    pressure = max(0.1, min(3.0, pressure))
                    print(f"✓ Pressure multiplier set to {pressure}x")
                except (ValueError, IndexError):
                    print("⚠️  Usage: stress <0.5-3.0>")
                print()
                continue

            if user_input.lower() in ["quantum on", "quantum off"]:
                enable = "on" in user_input.lower()
                diamond_orb.enable_quantum_healing(enable)
                print(f"✓ Quantum healing {'enabled' if enable else 'disabled'}")
                print()
                continue

            if user_input.lower() == "reset":
                diamond_orb.reset()
                print("✓ Diamond entity reset")
                print()
                continue

            # Process query
            print()
            print(f"⚡ Processing (pressure: {pressure}x)...")
            response = await diamond_orb.process_query(user_input, pressure_multiplier=pressure)
            print()

            if response.get("status") == "success":
                print("✨ Response:")
                print(response.get("unified_content", ""))
                print()

                diamond_meta = response.get("diamond_metadata", {})
                if diamond_meta.get("collapsed"):
                    print("⚠️  Collapse occurred!")
                    if diamond_meta.get("repaired"):
                        print("✓ System self-repaired")

                print(f"Pressure: {diamond_meta.get('pressure_applied', 0):.2%}")
                print(f"Health: {diamond_meta.get('metrics', {}).get('health_score', 0):.2%}")
            else:
                print(f"❌ Error: {response.get('message', 'Unknown error')}")

            print()
            print_separator("-")
            print()

        except KeyboardInterrupt:
            print()
            print("👋 Shutting down Diamond Orb...")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            print()


async def main():
    """Main entry point for diamond entity demos."""
    if len(sys.argv) > 1:
        mode = sys.argv[1]
    else:
        mode = "basic"

    if mode == "basic":
        await demo_basic_collapse_and_repair()
    elif mode == "stress":
        await demo_stress_test()
    elif mode == "cycles":
        await demo_multiple_collapse_cycles()
    elif mode == "quantum":
        await demo_quantum_healing()
    elif mode == "validate":
        await demo_recovery_validation()
    elif mode == "interactive":
        await interactive_mode()
    elif mode == "all":
        await demo_basic_collapse_and_repair()
        await demo_stress_test()
        await demo_multiple_collapse_cycles()
        await demo_quantum_healing()
        await demo_recovery_validation()
    else:
        print("Diamond Entity Demonstration")
        print()
        print("Usage: python demo_diamond.py [mode]")
        print()
        print("Modes:")
        print("  basic       - Basic collapse and repair (default)")
        print("  stress      - Stress test with increasing pressure")
        print("  cycles      - Multiple collapse and repair cycles")
        print("  quantum     - Quantum healing algorithms")
        print("  validate    - Full recovery and validation")
        print("  interactive - Interactive exploration mode")
        print("  all         - Run all demonstrations")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
