# CLI Chatbot with OpenAI Integration

A modular CLI chatbot that connects to OpenAI's Chat API with support for custom tools and functions. Features beautiful formatting using Rich and a modular architecture for easy tool registration.

## Features

- 🤖 OpenAI GPT integration with tool calling support
- 🎨 Beautiful CLI interface with Rich formatting
- 🔧 Modular tool system for easy extensibility
- 📁 Auto-discovery of tools from directory structure
- ⚙️ Environment-based configuration
- 💬 Interactive chat with conversation history

## Quick Start

1. **Clone and install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

3. **Run the chatbot:**
   ```bash
   python main.py
   ```

## Configuration

Configure the chatbot using environment variables in your `.env` file:

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `OPENAI_MODEL`: Model to use (default: gpt-4o-mini)
- `MAX_TOKENS`: Maximum tokens per response (default: 1000)
- `TEMPERATURE`: Response creativity (0.0-2.0, default: 0.7)
- `SYSTEM_PROMPT`: Custom system prompt

## Available Tools

The chatbot comes with several built-in tools:

### Calculator
- **Function**: `calculate`
- **Description**: Perform basic mathematical calculations
- **Example**: "What's 15 * 7 + 23?"

### File Operations
- **Function**: `file_operations`
- **Description**: Read files and list directory contents
- **Example**: "Show me the contents of the current directory"

### DateTime
- **Function**: `get_datetime`
- **Description**: Get current date and time in various formats
- **Example**: "What time is it now?"

## Creating Custom Tools

To create a custom tool:

1. Create a new Python file in `tools/available/`
2. Inherit from `BaseTool` and implement required methods:

```python
from typing import List
from tools.base import BaseTool, ToolParameter

class MyCustomTool(BaseTool):
    @property
    def name(self) -> str:
        return "my_tool"
    
    @property
    def description(self) -> str:
        return "Description of what my tool does"
    
    @property
    def parameters(self) -> List[ToolParameter]:
        return [
            ToolParameter(
                name="param1",
                type="string",
                description="Description of parameter"
            )
        ]
    
    def execute(self, param1: str) -> str:
        # Your tool logic here
        return f"Result: {param1}"
```

3. The tool will be automatically discovered and registered when the chatbot starts.

## Architecture

```
tool-use-chat/
├── chatbot/           # Main chatbot logic
│   ├── __init__.py
│   ├── bot.py         # ChatBot class
│   └── config.py      # Configuration management
├── tools/             # Tool system
│   ├── __init__.py
│   ├── base.py        # BaseTool abstract class
│   ├── registry.py    # Tool registry
│   └── available/     # Available tools directory
│       ├── calculator.py
│       ├── file_operations.py
│       └── datetime_tool.py
├── utils/             # Utilities
│   ├── __init__.py
│   ├── formatting.py  # Rich formatting functions
│   └── validators.py  # Validation utilities
├── main.py            # Entry point
├── .env.example       # Environment variables template
└── requirements.txt   # Dependencies
```

## Commands

While chatting, you can use these special commands:

- `help` - Show available commands and tools
- `tools` - List all registered tools
- `quit` or `exit` - Exit the chatbot

## Requirements

- Python 3.13+
- OpenAI API key
- Dependencies listed in requirements.txt

## License

This project is open source and available under the MIT License.
