# AMW Link Proxies

Prefect Horizon–hosted FastMCP proxy servers for Short.io and Linkly.
These servers inject API credentials server-side, so Claude.ai connectors
require no auth header configuration on the client.

## Servers

### Short.io (`shortio_proxy.py`)
Proxies to `https://ai-assistant.short.io/mcp`.
Use for: link analytics, domain stats, top column reports, link search.
Not for: creating/editing links (handled by Make.com via Grist).

### Linkly (`linkly_proxy.py`)
Proxies to `https://mcp.linklyhq.com`.
Use for: analytics, OG field iteration on personalised links,
webhook management, link updates.

## Deployment (Prefect Horizon)

Each file is deployed as a **separate Horizon server**.

### Short.io
- Entrypoint: `shortio_proxy.py:mcp`
- Environment secrets: `SHORTIO_API_KEY`

### Linkly
- Entrypoint: `linkly_proxy.py:mcp`
- Environment secrets: `LINKLY_API_KEY`, `LINKLY_WORKSPACE_ID`

## Local verification

```bash
pip install fastmcp
fastmcp inspect shortio_proxy.py:mcp
fastmcp inspect linkly_proxy.py:mcp
```
