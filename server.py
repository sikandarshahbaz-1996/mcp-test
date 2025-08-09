from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def greeting(name: str) -> str:
    """
    Args:
        name (str): The name of the person to greet.
    """

    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")