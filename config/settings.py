# ============================================================================
# APPLICATION SETTINGS FOR VESPUCCI.AI PLATFORM
# ============================================================================
# Settings for working with various MCP servers

from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load environment variables from .env file if present
load_dotenv()


class Settings(BaseSettings):
    """Application settings loaded from environment variables
    
    This class defines the configuration settings for the application,
    configured for connecting to various MCP servers.
    """
    # MCP Server Configuration
    # Instead of a path to a script, we'll use a command and arguments
    # to run the MCP server with npx
    mcp_command: str = "npx"
    mcp_args: list = ["-y", "web3-research-mcp@latest"]  # Default MCP server, can be changed
    
    # Discord Bot Configuration
    discord_enabled: bool = True
    discord_command_prefix: str = "!"


# Create a singleton instance of the settings
settings = Settings()