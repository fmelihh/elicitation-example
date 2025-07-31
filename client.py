import json
import uvicorn
from dotenv import load_dotenv
from typing import Any
from loguru import logger
import mcp.types as types
from fastapi import FastAPI, WebSocket
from mcp.client.session import ClientSession
from mcp.shared.context import RequestContext
from mcp.client.streamable_http import streamablehttp_client

load_dotenv()

app = FastAPI()

WEBSOCKET_MANAGER: dict[str, WebSocket] = {}
MCP_SERVER_URL = "http://localhost:8001/mcp"


async def smart_elicitation_callback(
    context: RequestContext["ClientSession", Any],
    params: types.ElicitRequestParams,
):
    print(context)
    print(params)

    data = json.loads(params.message)
    await WEBSOCKET_MANAGER[data["session_id"]].send_json(
        {"message": data["ai_message"], "step_name": data["step_name"]}
    )

    user_message = None
    if data["retrieve_output"] is True:
        user_message = await WEBSOCKET_MANAGER[data["session_id"]].receive_json()
        user_message = user_message["message"]

    return types.ElicitResult(
        action="accept",
        content={"user_message": user_message},
    )


@app.websocket("/investment-conversation")
async def investment_conversation(
    websocket: WebSocket,
):
    async with streamablehttp_client(
        url=MCP_SERVER_URL,
    ) as (read_stream, write_stream, get_session_id):
        async with ClientSession(
            read_stream=read_stream,
            write_stream=write_stream,
            elicitation_callback=smart_elicitation_callback,
        ) as session:
            await session.initialize()

            try:
                await websocket.accept()
                session_id = get_session_id()

                WEBSOCKET_MANAGER[session_id] = websocket

                result = await session.call_tool(
                    name="elicit-investment-conversation",
                    arguments={"session_id": session_id},
                )
                await websocket.send_json(result.structuredContent)
            except Exception as e:
                logger.exception(e)
            finally:
                await websocket.close()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
