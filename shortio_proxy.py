"""
Short.io MCP Proxy Server
Proxies to https://ai-assistant.short.io/mcp with API key auth injected server-side.
Deployed to Prefect Horizon — exposes Short.io analytics & link search to Claude.
"""

import os
from fastmcp.server import create_proxy
from fastmcp.client import Client
from fastmcp.client.transports import SSETransport

SHORTIO_API_KEY = os.environ["SHORTIO_API_KEY"]
SHORTIO_MCP_URL = "https://ai-assistant.short.io/mcp"

transport = SSETransport(
    url=SHORTIO_MCP_URL,
    headers={"Authorization": SHORTIO_API_KEY},
)

mcp = create_proxy(Client(transport), name="shortio_mcp")
