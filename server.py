from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Greeting")

@mcp.tool()
def greeting(name: str) -> str:
    return f"Hello, {name}!"

app = mcp.app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
