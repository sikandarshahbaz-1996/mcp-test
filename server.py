from mcp.server.fastmcp import FastMCP

mcp = FastMCP("greeting")

@mcp.tool()
def greeting(name: str) -> str:
    """
    Args:
        name (str): The name of the person to greet.
    """

    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        uvicorn_kwargs={"host": "0.0.0.0", "port": 8000}
    )

