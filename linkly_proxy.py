"""
Linkly MCP Proxy Server
Proxies to https://mcp.linklyhq.com with API key auth injected server-side.
Deployed to Prefect Horizon — exposes Linkly link management & analytics to Claude.

Linkly tools available:
  create_link, update_link, delete_link, get_link, list_links, search_links,
  get_clicks, get_analytics, get_analytics_by, list_domains,
  list_webhooks, subscribe_webhook
"""

import os
from fastmcp.server import create_proxy
from fastmcp.client import Client
from fastmcp.client.transports import StreamableHttpTransport

LINKLY_API_KEY = os.environ["LINKLY_API_KEY"]
LINKLY_WORKSPACE_ID = os.environ.get("LINKLY_WORKSPACE_ID", "296177")
LINKLY_MCP_URL = "https://mcp.linklyhq.com"

transport = StreamableHttpTransport(
    url=LINKLY_MCP_URL,
    headers={
        "Authorization": f"Bearer {LINKLY_API_KEY}",
        "X-Workspace-ID": LINKLY_WORKSPACE_ID,
    },
)

mcp = create_proxy(Client(transport), name="linkly_mcp")
