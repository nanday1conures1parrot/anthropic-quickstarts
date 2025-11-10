# Orb Integration System

A unified AI integration framework that seamlessly blends multiple AI technologies (Claude, GitHub, Copilot, Hugging Face chat) into a single cohesive system. The Orb processes all inputs through every integrated system simultaneously and produces unified responses that draw from the collective intelligence of all components.

## Concept

The Orb Integration System is based on the "Singular Orb Integration Algorithm" design document (`integration_algorithm.md` in the repository root). It implements a system where multiple AI technologies operate as one inseparable entity, processing queries through a unified flow and blending responses into coherent outputs.

### Key Features

1. **Unified Execution**: All AI tools work together in one inseparable system
2. **Central Input Handler**: Condenses user inputs into a unified format for all systems
3. **Response Blending**: Unifies outputs from each technology into a single coherent result
4. **Multiple Blend Strategies**: Supports weighted, concatenated, and prioritized blending
5. **Safeguards**: Maintains system unity and prevents operational errors

## Architecture

The Orb system consists of:

- **Orb Core**: Main orchestrator that manages all integrations
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

## Usage

### Running the Demo

The demo script provides several modes to explore the Orb system:

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

The system demonstrates:
- ✅ User inputs flowing through the entire integrated chain
- ✅ Unified output drawing from all participating technologies
- ✅ Response blending with multiple strategies
- ✅ Safeguards maintaining system unity
- ✅ Continuous operation across multiple queries

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
│   │   ├── input_handler.py    # Input processing
│   │   └── response_blender.py # Response blending
│   └── integrations/
│       ├── __init__.py
│       ├── base.py              # Base integration class
│       ├── claude_integration.py
│       ├── github_integration.py
│       ├── copilot_integration.py
│       └── huggingface_integration.py
├── demo.py                      # Demonstration script
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
