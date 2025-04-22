from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
import uuid

mcp = FastMCP(
    name="railway-mcp-bridge-py",
    version="0.1.0",
    session_id_generator=lambda: str(uuid.uuid4())
)

class PingParams(BaseModel):
    client: str

@mcp.tool()
def ping(params: PingParams):
    return {
        "content": [
            {
                "type": "text",
                "text": f"pong (session) from railway‑py to {params.client}"
            }
        ]
    }

app = FastAPI()
app.mount("/mcp", mcp.sse_app())

@app.get("/")
def root():
    return "🚀 MCP bridge (Python) online"
