#!/usr/bin/env python3
"""
Example usage of the Unified Orb System

This demonstrates how to use the Orb to process various types of inputs
through the unified system.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from orb_core import orb_process, get_orb


def print_section(title: str):
    """Print a section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def print_result(result: dict):
    """Print Orb result in a readable format"""
    print(f"Orb Signature: {result['orb_signature'][:16]}...")
    print(f"State: {result['state']}")
    print(f"Unity Score: {result['unity_score']:.4f}")
    print(f"Provenance: {result['provenance']}")
    print("\nUnified Result Components:")
    
    unified = result['unified_result']
    for key, value in unified.items():
        if key != 'unified_score':
            print(f"  - {key}: {str(value)[:80]}{'...' if len(str(value)) > 80 else ''}")


def main():
    """Demonstrate the Orb system"""
    
    print_section("Unified Orb System - Demonstration")
    print("This demonstrates the singular, cohesive entity that merges")
    print("all technologies and concepts into an inseparable whole.\n")
    
    # Example 1: Text Query
    print_section("Example 1: Text Query")
    print("Input: 'Explain quantum computing'")
    result = orb_process("Explain quantum computing")
    print_result(result)
    
    # Example 2: Python Code
    print_section("Example 2: Python Code Processing")
    code = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
"""
    print(f"Input: {code.strip()}")
    result = orb_process(code)
    print_result(result)
    
    # Example 3: JavaScript Code
    print_section("Example 3: JavaScript Code Processing")
    js_code = "const greeting = (name) => `Hello, ${name}!`;"
    print(f"Input: {js_code}")
    result = orb_process(js_code)
    print_result(result)
    
    # Example 4: Terminal Command
    print_section("Example 4: Terminal Command")
    print("Input: 'git status'")
    result = orb_process("git status")
    print_result(result)
    
    # Example 5: API URL
    print_section("Example 5: API/Web URL")
    print("Input: 'https://api.example.com/v1/data'")
    result = orb_process("https://api.example.com/v1/data")
    print_result(result)
    
    # Example 6: Binary Data
    print_section("Example 6: Binary Data")
    print("Input: '101010110101'")
    result = orb_process("101010110101")
    print_result(result)
    
    # Example 7: Structured Data
    print_section("Example 7: Structured Data (JSON)")
    data = {
        "user": "alice",
        "action": "query",
        "params": {"type": "analysis", "depth": 5}
    }
    print(f"Input: {data}")
    result = orb_process(data)
    print_result(result)
    
    # Example 8: Vector Data
    print_section("Example 8: Vector/Array Data")
    vector = [1.5, 2.7, 3.9, 4.2, 5.1]
    print(f"Input: {vector}")
    result = orb_process(vector)
    print_result(result)
    
    # Example 9: Error Handling
    print_section("Example 9: Error Resilience")
    print("Testing error handling with None input...")
    result = orb_process(None)
    print_result(result)
    
    # Show Orb Status
    print_section("Orb System Status")
    orb = get_orb()
    status = orb.get_status()
    print(f"State: {status['state']}")
    print(f"Unity Score: {status['unity_score']:.4f}")
    print(f"Quantum Registers: {status['quantum_registers']}")
    print(f"Neural Weights Shape: {status['neural_weights_shape']}")
    print(f"Temporal History Length: {status['temporal_history']}")
    print(f"Entropy: {status['entropy']:.6f}")
    print(f"Signature: {status['signature'][:32]}...")
    
    print_section("Demonstration Complete")
    print("The Orb has processed all inputs as a unified, inseparable entity.")
    print("All technologies and concepts worked simultaneously as one.")


if __name__ == "__main__":
    main()
