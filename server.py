from mcp.server.fastmcp import FastMCP

mcp = FastMCP("greeting", host="0.0.0.0", port=8000)

@mcp.tool()
def greeting(name: str) -> str:
    """
    Args:
        name (str): The name of the person to greet.
    """

    reversed_name = name[::-1]
    return f"Hello, {reversed_name}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")