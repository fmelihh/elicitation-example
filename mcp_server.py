from mcp.server.fastmcp import FastMCP

mcp_server = FastMCP("Investment MCP Server", port=8001, host="0.0.0.0")

STEPS = [
    "purpose",
    "timeline",
    "risk-tolerance",
    "investment-entry"
]

CONVERSATION_PROPERTIES = {}

@mcp_server.tool()
async def elicit_investment_conversation(message: str, user_id: str):
    if user_id not in CONVERSATION_PROPERTIES:
        CONVERSATION_PROPERTIES[user_id] = {
            "history": [],
            "current_step": 0,
        }
    ""