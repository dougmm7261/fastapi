from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
import uuid

mcp = FastMCP(
    name="railway‑mcp‑bridge",
    version="0.1.0",
    session_id_generator=lambda: str(uuid.uuid4())
)

class PingParams(BaseModel):
    client: str

@mcp.tool()
def ping(params: PingParams):
    return {
        "content": [
            { "type": "text",
              "text": f"pong → {params.client}" }
        ]
    }

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# works with **/mcp** and **/mcp/**
app.include_router(mcp.router, prefix="/mcp")

@app.get("/")
def root():
    return {"status": "online"}
