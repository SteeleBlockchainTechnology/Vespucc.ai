# Vespucci.ai Platform

Vespucci.ai is a versatile AI platform that connects to various MCP (Machine Conversation Protocol) servers, enabling powerful AI interactions through multiple interfaces including a REST API and Discord bot integration.

## Overview

Vespucci.ai serves as a bridge between users and AI capabilities provided by MCP servers. The platform uses Groq's language models to process user queries and interact with tools provided by the connected MCP server.

### Key Features

- **MCP Server Integration**: Connect to any compatible MCP server to access its tools and capabilities
- **Groq LLM Integration**: Leverages Groq's powerful language models for natural language processing
- **Discord Bot**: Interact with the AI through Discord channels and direct messages
- **REST API**: Programmatically access AI capabilities through a FastAPI backend
- **Tool Orchestration**: Dynamically discovers and utilizes tools provided by the connected MCP server
- **Conversation Logging**: Maintains logs of all conversations for reference and debugging

## Architecture

Vespucci.ai follows a modular architecture:

- **MCP Client**: Core component that connects to MCP servers and manages tool interactions
- **Language Model Client**: Interfaces with Groq's API for LLM capabilities
- **Discord Bot**: Provides a chat interface through Discord
- **FastAPI Server**: Exposes REST endpoints for programmatic access
- **Configuration System**: Manages settings and environment variables

## Prerequisites

- Python 3.10 or higher
- Node.js v16 or higher (required for MCP servers)
- Groq API key
- Discord Bot Token (optional, for Discord integration)

## Installation

### Using Poetry (Recommended)

```bash
# Clone the repository
git clone https://github.com/your-username/vespucci.ai.git
cd vespucci.ai/mcp

# Install dependencies using Poetry
pip install poetry
poetry install
```

### Environment Setup

Create a `.env` file in the project root with the following variables:

```
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3-8b-8192  # Optional, this is the default
DISCORD_TOKEN=your_discord_bot_token_here  # Optional, for Discord integration
```

A sample `.env.example` file is provided for reference.

## Usage

### Starting the Platform

```bash
# Using Poetry
poetry run python main.py

# Or directly with Python if not using Poetry
python main.py
```

This will:

1. Start the FastAPI server
2. Connect to the configured MCP server
3. Initialize the Discord bot (if token is provided)

### Connecting to Different MCP Servers

By default, Vespucci.ai connects to the `web3-research-mcp` server. You can change this in the `config/settings.py` file or by setting environment variables.

```python
# In config/settings.py
mcp_args: list = ["--yes", "your-preferred-mcp-server@latest"]
```

### Using the Discord Bot

Once the platform is running with a valid Discord token:

1. Invite the bot to your server using the OAuth2 URL from the Discord Developer Portal
2. Interact with the bot using the configured command prefix (default: `!`)
3. Example: `!ask What is the current price of Ethereum?`

### Using the REST API

The platform exposes several endpoints:

- `POST /api/query` - Send a query to the AI

  ```json
  {
    "query": "What is the current price of Ethereum?"
  }
  ```

- `GET /api/tools` - List available tools from the connected MCP server

## Extending Vespucci.ai

### Creating Custom MCP Servers

Vespucci.ai can connect to any MCP-compatible server. To create your own:

1. Follow the MCP protocol specification
2. Implement the required tool interfaces
3. Publish your server as an npm package or provide a direct path to your script

### Adding New Features

The modular architecture makes it easy to extend:

- Add new API routes in `api/routes.py`
- Extend Discord bot commands in `discord_bot/commands.py`
- Modify LLM behavior in `client/language_model.py`

## Conversation Logging

All conversations are logged to the `conversations/` directory in JSON format, with timestamps for easy reference.

## Troubleshooting

### Common Issues

- **MCP Server Connection Failure**: Ensure Node.js is installed and the MCP server package is accessible
- **Groq API Errors**: Verify your API key is correct and has sufficient quota
- **Discord Bot Not Responding**: Check that the token is valid and the bot has proper permissions

## License

[Specify your license here]

## Acknowledgements

- [Groq](https://groq.com/) for providing the LLM API
- [MCP Protocol](https://github.com/microsoft/mcp) for the tool orchestration framework
- [Discord.py](https://discordpy.readthedocs.io/) for Discord integration
- [FastAPI](https://fastapi.tiangolo.com/) for the REST API framework
