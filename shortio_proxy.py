"""
Short.io MCP Proxy Server
Proxies to https://ai-assistant.short.io/mcp with API key auth injected server-side.
Deployed to Prefect Horizon — exposes Short.io analytics & link search to Claude.
"""

import os
from fastmcp import FastMCP, Client

SHORTIO_API_KEY = os.environ["SHORTIO_API_KEY"]
SHORTIO_MCP_URL = "https://ai-assistant.short.io/mcp"

client = Client(
    SHORTIO_MCP_URL,
    headers={"Authorization": SHORTIO_API_KEY},
)

mcp = FastMCP.as_proxy(client, name="shortio_mcp")
