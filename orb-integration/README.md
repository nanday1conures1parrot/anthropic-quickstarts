# Orb Integration System

A unified AI integration framework that seamlessly blends multiple AI technologies (Claude, GitHub, Copilot, Hugging Face chat) into a single cohesive system. The Orb processes all inputs through every integrated system simultaneously and produces unified responses that draw from the collective intelligence of all components.

**NEW: Diamond Entity** - Self-healing system with computational collapse and repair capabilities that transforms extreme pressure into optimized structure.

## Concept

The Orb Integration System is based on the "Singular Orb Integration Algorithm" design document (`integration_algorithm.md` in the repository root). It implements a system where multiple AI technologies operate as one inseparable entity, processing queries through a unified flow and blending responses into coherent outputs.

### Key Features

1. **Unified Execution**: All AI tools work together in one inseparable system
2. **Central Input Handler**: Condenses user inputs into a unified format for all systems
3. **Response Blending**: Unifies outputs from each technology into a single coherent result
4. **Multiple Blend Strategies**: Supports weighted, concatenated, and prioritized blending
5. **Safeguards**: Maintains system unity and prevents operational errors
6. **Diamond Entity** (NEW): Self-repair system with:
   - Computational collapse simulation
   - Neural network-inspired self-healing
   - Quantum healing algorithms
   - Automatic pressure detection and recovery
   - Modular destruction and reconstruction

## Architecture

The Orb system consists of:

- **Orb Core**: Main orchestrator that manages all integrations
- **Diamond Entity**: Self-repair system for collapse detection and healing
- **Diamond Orb**: Integration of Orb with Diamond Entity capabilities
- **Input Handler**: Transforms user queries into unified format
- **Response Blender**: Combines responses from all integrations
- **Integrations**:
  - Claude AI (full integration with Anthropic API)
  - GitHub (contextual repository insights)
  - GitHub Copilot (code suggestions and patterns)
  - Hugging Face (specialized model capabilities)

## Installation

1. Clone this repository
2. Navigate to the orb-integration directory:
   ```bash
   cd orb-integration
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   ```

4. Set up your Claude API key:
   ```bash
   export ANTHROPIC_API_KEY=your_api_key_here
   ```

## Diamond Entity: Self-Healing System

The Diamond Entity is an advanced self-repair system that embodies computational resilience. Like carbon under extreme pressure forming a diamond, the system transforms computational chaos into optimized, crystalline structure.

### Key Concepts

**Collapse Mechanism**: The system simulates extreme computational overload through:
- Contradictory logic paths that create logical conflicts
- Memory overflow conditions that stress system resources
- Deep recursive calls that max out execution thresholds
- Dynamic pressure monitoring and threshold detection

**Self-Repair Logic**: When collapse is detected, the system automatically:
- Detects outliers and redundant code patterns
- Fuses outliers into optimized, reusable modules
- Resolves contradictions using neural-inspired algorithms
- Flattens recursive patterns into iterative structures
- Unifies disparate integrations into cohesive whole
- Applies quantum-inspired healing for advanced optimization

**Singular Entity Design**: The Diamond Orb creates a unified system that:
- Merges all AI technologies into one inseparable entity
- Maintains cohesion even during collapse scenarios
- Reconstructs itself into an optimized state after failure
- Demonstrates organic recovery without external intervention

### Diamond Entity Features

1. **Pressure Monitoring**: Real-time tracking of computational pressure levels
2. **Collapse Detection**: Automatic detection when thresholds are exceeded
3. **Outlier Fusion**: Intelligent merging of redundant patterns
4. **Contradiction Resolution**: Ternary logic for conflict resolution
5. **Recursive Flattening**: Optimization of deep call stacks
6. **Integration Unification**: Cohesive blending of all components
7. **Quantum Healing**: Superposition-inspired optimization algorithms
8. **State Snapshots**: Recovery points for emergency restoration
9. **Metrics Export**: Comprehensive tracking of health and repairs

## Usage

### Running the Diamond Entity Demo

The Diamond Entity demo showcases self-repair capabilities:

#### Basic Collapse and Repair
```bash
python demo_diamond.py basic
```

Demonstrates a collapse scenario under high pressure and automatic self-repair.

#### Stress Test
```bash
python demo_diamond.py stress
```

Tests the system with increasing pressure levels (0.5x to 2.0x).

#### Multiple Cycles
```bash
python demo_diamond.py cycles
```

Shows multiple collapse and repair cycles demonstrating continuous operation.

#### Quantum Healing
```bash
python demo_diamond.py quantum
```

Demonstrates quantum-inspired healing algorithms in action.

#### Full Validation
```bash
python demo_diamond.py validate
```

Complete validation sequence proving organic recovery and singular entity emergence.

#### Interactive Mode
```bash
python demo_diamond.py interactive
```

Explore the Diamond Entity interactively with custom queries and pressure levels.

#### All Demonstrations
```bash
python demo_diamond.py all
```

Run all demonstrations in sequence.

### Using the Diamond Orb in Your Code

```python
import asyncio
from orb_integration.core import DiamondOrb

async def main():
    # Initialize the Diamond Orb
    diamond_orb = DiamondOrb(
        anthropic_api_key="your_api_key",
        collapse_threshold=0.85,  # 85% pressure triggers collapse
        enable_quantum_healing=True,  # Enable advanced healing
        blend_strategy="weighted"
    )
    
    # Process a query with pressure monitoring
    response = await diamond_orb.process_query(
        query="Optimize this complex algorithm",
        pressure_multiplier=1.5  # Apply 1.5x pressure
    )
    
    # Check if collapse occurred
    if response["diamond_metadata"]["collapsed"]:
        print("System collapsed and repaired!")
        print(f"Repair details: {response['diamond_metadata']['repair_details']}")
    
    # View system status
    status = diamond_orb.get_status()
    print(f"System state: {status['system_state']}")
    print(f"Health score: {status['diamond']['metrics']['health_score']:.2%}")

asyncio.run(main())
```

### Stress Testing Example

```python
# Run a comprehensive stress test
results = await diamond_orb.stress_test(
    "Process this intensive workload",
    pressure_levels=[0.5, 1.0, 1.5, 2.0, 2.5]
)

print(f"Max pressure survived: {results['max_pressure_survived']}x")
print(f"Collapses: {results['collapse_count']}")
print(f"Repairs: {results['repair_count']}")
```

### Running the Original Orb Demo

The original demo script provides several modes to explore the base Orb system:

#### Basic Demo (Single Query)
```bash
python demo.py basic
```

Demonstrates a single query processed through all integrations with a unified response.

#### Multiple Queries Demo
```bash
python demo.py multiple
```

Shows multiple queries processed sequentially, demonstrating the Orb's continuous operation.

#### Blend Strategies Demo
```bash
python demo.py strategies
```

Demonstrates different response blending strategies (weighted, concatenate, prioritize).

#### Interactive Mode
```bash
python demo.py interactive
```

Run the Orb in interactive mode where you can enter your own queries in real-time.

### Using the Orb in Your Code

```python
import asyncio
from orb_integration.core import Orb

async def main():
    # Initialize the Orb
    orb = Orb(
        anthropic_api_key="your_api_key",
        blend_strategy="weighted"  # or "concatenate" or "prioritize"
    )
    
    # Process a query
    response = await orb.process_query(
        query="How do I optimize my database queries?",
        context={"language": "Python"}
    )
    
    # Access the unified response
    if response["status"] == "success":
        print(response["unified_content"])
        print(f"Sources: {response['sources']}")

asyncio.run(main())
```

## Blend Strategies

The Orb supports three response blending strategies:

### Weighted (Default)
Blends responses with importance weights assigned to each source:
- Claude AI: 40%
- GitHub Copilot: 25%
- GitHub: 20%
- Hugging Face: 15%

### Concatenate
Sequentially combines all responses, preserving full content from each source.

### Prioritize
Uses the highest-priority source as the primary response, with others as supporting context.

## System Status

Check the Orb's status at any time:

```python
status = orb.get_status()
print(f"Executions: {status['execution_count']}")
print(f"Health: {status['system_health']}")
```

## Integration Details

### Claude AI Integration
- **Status**: Full implementation
- **Features**: Natural language understanding, code analysis, explanations
- **Requirements**: ANTHROPIC_API_KEY environment variable

### GitHub Integration
- **Status**: Simulated (mock implementation)
- **Features**: Repository context, collaboration patterns, code insights
- **Note**: Full implementation would connect to GitHub API

### GitHub Copilot Integration
- **Status**: Simulated (mock implementation)
- **Features**: Code suggestions, debugging patterns, refactoring recommendations
- **Note**: Full implementation would connect to Copilot services

### Hugging Face Integration
- **Status**: Simulated (mock implementation)
- **Features**: Specialized models, embeddings, multi-modal capabilities
- **Note**: Full implementation would connect to Hugging Face Inference API

## Testing

Run the test suite to verify all functionality:

```bash
pytest tests/ -v
```

The system demonstrates:
- ✅ User inputs flowing through the entire integrated chain
- ✅ Unified output drawing from all participating technologies
- ✅ Response blending with multiple strategies
- ✅ Safeguards maintaining system unity
- ✅ Continuous operation across multiple queries
- ✅ Computational collapse detection and simulation (Diamond Entity)
- ✅ Automatic self-repair and healing (Diamond Entity)
- ✅ Outlier detection and fusion (Diamond Entity)
- ✅ Quantum-inspired optimization (Diamond Entity)
- ✅ Emergency recovery and state restoration (Diamond Entity)

Run the demos to see these features in action!

## Example Output

```
📝 User Query: How can I write a Python function to optimize database queries?

⚡ Processing through all integrations...

─────────────────────────────────────────────────────────────────
✨ UNIFIED ORB RESPONSE
─────────────────────────────────────────────────────────────────

[Claude AI] ●●●●
Here's a comprehensive approach to writing Python functions for database query optimization...

──────────────────────────────────────────────────────────────────

[GitHub Copilot] ●●●
Code structure patterns identified
Best practices recommendations available

──────────────────────────────────────────────────────────────────

[GitHub] ●●
Repository context analysis available
Recent commits and issues reviewed

──────────────────────────────────────────────────────────────────

[Hugging Face] ●●
General-purpose models available
Embedding and similarity analysis ready

─────────────────────────────────────────────────────────────────
✓ Sources: Claude AI, GitHub Copilot, GitHub, Hugging Face
✓ Blend Strategy: weighted
✓ Successful: 4
✓ Failed: 0
✓ Execution ID: 1
✓ Unity Preserved: True
```

## Development

### Project Structure
```
orb-integration/
├── orb_integration/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── orb.py              # Main orchestrator
│   │   ├── diamond_entity.py   # Self-repair system (NEW)
│   │   ├── diamond_orb.py      # Diamond Orb integration (NEW)
│   │   ├── input_handler.py    # Input processing
│   │   └── response_blender.py # Response blending
│   └── integrations/
│       ├── __init__.py
│       ├── base.py              # Base integration class
│       ├── claude_integration.py
│       ├── github_integration.py
│       ├── copilot_integration.py
│       └── huggingface_integration.py
├── tests/
│   ├── __init__.py
│   ├── test_orb.py
│   └── test_diamond_entity.py  # Diamond Entity tests (NEW)
├── demo.py                      # Original Orb demonstration
├── demo_diamond.py              # Diamond Entity demonstration (NEW)
├── pyproject.toml
└── README.md
```

### Adding Custom Integrations

You can extend the Orb with custom integrations:

```python
from orb_integration.integrations import BaseIntegration

class CustomIntegration(BaseIntegration):
    def __init__(self):
        super().__init__(name="Custom Service")
    
    async def process(self, unified_input):
        # Your integration logic here
        return {
            "source": self.name,
            "status": "success",
            "content": "Your response"
        }

# Add to Orb
orb.add_integration(CustomIntegration())
```

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## Acknowledgments

This implementation is based on the "Singular Orb Integration Algorithm" design document, which prescribes a unified approach to integrating multiple AI technologies into an inseparable system.
