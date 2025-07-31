import uvicorn
from fastapi import FastAPI

app = FastAPI()
MCP_SERVER_URL = "http://localhost:8001/mcp"


@app.get("/investment-conversation")
async def investment_conversation(message: str, user_id: str):



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
