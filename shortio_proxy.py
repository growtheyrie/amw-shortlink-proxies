"""
Short.io MCP Proxy Server
Proxies to https://ai-assistant.short.io/mcp with API key auth injected server-side.
Deployed to Prefect Horizon — exposes Short.io analytics & link search to Claude.
"""

import os
from fastmcp import FastMCP
from fastmcp.server import create_proxy
from fastmcp.client.transports import StreamableHttpTransport

SHORTIO_API_KEY = os.environ["SHORTIO_API_KEY"]
SHORTIO_MCP_URL = "https://ai-assistant.short.io/mcp"

transport = StreamableHttpTransport(
    url=SHORTIO_MCP_URL,
    headers={"Authorization": f"Bearer {SHORTIO_API_KEY}"},
)

mcp = create_proxy(
    transport,
    name="shortio_mcp",
)
