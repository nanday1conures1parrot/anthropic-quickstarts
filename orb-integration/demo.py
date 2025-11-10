#!/usr/bin/env python3
"""
Orb Integration System Demo

This script demonstrates the unified Orb system processing user queries
through multiple AI integrations simultaneously and producing blended responses.
"""

import asyncio
import os
import sys

from orb_integration.core import Orb


async def demo_basic_query():
    """Demonstrate a basic query through the Orb system."""
    print("=" * 70)
    print("ORB INTEGRATION SYSTEM - BASIC QUERY DEMO")
    print("=" * 70)
    print()

    # Initialize the Orb
    orb = Orb(anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY"), blend_strategy="weighted")

    # Show system status
    status = orb.get_status()
    print("🌐 Orb System Status:")
    print(f"   Active Integrations: {len([i for i in status['integrations'] if i['enabled']])}")
    for integration in status["integrations"]:
        status_icon = "✓" if integration["enabled"] else "✗"
        print(f"   {status_icon} {integration['name']}")
    print()

    # Process a query
    query = "How can I write a Python function to optimize database queries?"
    print(f"📝 User Query: {query}")
    print()
    print("⚡ Processing through all integrations...")
    print()

    response = await orb.process_query(query)

    # Display results
    print("─" * 70)
    print("✨ UNIFIED ORB RESPONSE")
    print("─" * 70)
    print()

    if response.get("status") == "success":
        print(response.get("unified_content", ""))
        print()
        print("─" * 70)
        print(f"✓ Sources: {', '.join(response.get('sources', []))}")
        print(f"✓ Blend Strategy: {response.get('blend_strategy', 'unknown')}")
        print(f"✓ Successful: {response.get('successful_integrations', 0)}")
        print(f"✓ Failed: {response.get('failed_integrations', 0)}")

        metadata = response.get("orb_metadata", {})
        print(f"✓ Execution ID: {metadata.get('execution_id', 'N/A')}")
        print(f"✓ Unity Preserved: {metadata.get('unity_preserved', False)}")
    else:
        print(f"❌ Error: {response.get('message', 'Unknown error')}")

    print()


async def demo_multiple_queries():
    """Demonstrate multiple queries to show the Orb's continuous operation."""
    print()
    print("=" * 70)
    print("ORB INTEGRATION SYSTEM - MULTIPLE QUERIES DEMO")
    print("=" * 70)
    print()

    # Initialize the Orb
    orb = Orb(anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY"), blend_strategy="weighted")

    queries = [
        "How do I debug a memory leak in my application?",
        "What are best practices for API design?",
        "Help me refactor this code for better performance",
    ]

    for i, query in enumerate(queries, 1):
        print(f"📝 Query {i}: {query}")
        response = await orb.process_query(query)

        if response.get("status") == "success":
            print("✓ Processed successfully")
            print(f"  Sources: {', '.join(response.get('sources', []))}")
            metadata = response.get("orb_metadata", {})
            print(f"  Execution ID: {metadata.get('execution_id', 'N/A')}")
        else:
            print(f"❌ Error: {response.get('message', 'Unknown error')}")
        print()

    # Show final system status
    status = orb.get_status()
    print("─" * 70)
    print("🌐 Final Orb System Status:")
    print(f"   Total Executions: {status['execution_count']}")
    print(f"   System Health: {status['system_health']}")
    print()


async def demo_blend_strategies():
    """Demonstrate different blending strategies."""
    print()
    print("=" * 70)
    print("ORB INTEGRATION SYSTEM - BLEND STRATEGIES DEMO")
    print("=" * 70)
    print()

    query = "Create a function to validate user input"
    strategies = ["weighted", "concatenate", "prioritize"]

    for strategy in strategies:
        print(f"🔄 Testing '{strategy}' blend strategy...")
        print()

        orb = Orb(anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY"), blend_strategy=strategy)

        response = await orb.process_query(query)

        if response.get("status") == "success":
            print(f"✓ Strategy: {response.get('blend_strategy', 'unknown')}")
            print(f"  Sources: {', '.join(response.get('sources', []))}")

            # Show abbreviated content
            content = response.get("unified_content", "")
            if len(content) > 200:
                print(f"  Content preview: {content[:200]}...")
            else:
                print(f"  Content preview: {content}")
        else:
            print(f"❌ Error: {response.get('message', 'Unknown error')}")

        print()
        print("─" * 70)
        print()


async def interactive_mode():
    """Run the Orb in interactive mode."""
    print()
    print("=" * 70)
    print("ORB INTEGRATION SYSTEM - INTERACTIVE MODE")
    print("=" * 70)
    print()
    print("Enter your queries to process through the unified Orb system.")
    print("Type 'quit' or 'exit' to stop, 'status' to see system status.")
    print()

    orb = Orb(anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY"), blend_strategy="weighted")

    while True:
        try:
            query = input("📝 Your query: ").strip()

            if not query:
                continue

            if query.lower() in ["quit", "exit"]:
                print("👋 Shutting down Orb system...")
                break

            if query.lower() == "status":
                status = orb.get_status()
                print()
                print("🌐 Orb System Status:")
                print(f"   Executions: {status['execution_count']}")
                print(f"   Health: {status['system_health']}")
                print(f"   Strategy: {status['blend_strategy']}")
                for integration in status["integrations"]:
                    status_icon = "✓" if integration["enabled"] else "✗"
                    print(f"   {status_icon} {integration['name']}")
                print()
                continue

            print()
            print("⚡ Processing...")
            response = await orb.process_query(query)
            print()

            if response.get("status") == "success":
                print("✨ Unified Response:")
                print(response.get("unified_content", ""))
                print()
                print(f"Sources: {', '.join(response.get('sources', []))}")
            else:
                print(f"❌ Error: {response.get('message', 'Unknown error')}")

            print()
            print("─" * 70)
            print()

        except KeyboardInterrupt:
            print()
            print("👋 Shutting down Orb system...")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            print()


async def main():
    """Main entry point for the demo."""
    if len(sys.argv) > 1:
        mode = sys.argv[1]
    else:
        mode = "basic"

    if mode == "basic":
        await demo_basic_query()
    elif mode == "multiple":
        await demo_multiple_queries()
    elif mode == "strategies":
        await demo_blend_strategies()
    elif mode == "interactive":
        await interactive_mode()
    else:
        print("Usage: python demo.py [basic|multiple|strategies|interactive]")
        print()
        print("Modes:")
        print("  basic       - Single query demonstration (default)")
        print("  multiple    - Multiple queries demonstration")
        print("  strategies  - Different blending strategies demonstration")
        print("  interactive - Interactive query mode")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
