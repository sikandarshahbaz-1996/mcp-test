from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(location: str) -> str:
    """
    Get the current weather for a specified location.
    Args:
        location (str): The name of the location to get the weather for.
    """

    return f"The current weather in {location} is sunny with a temperature of 25°C."

if __name__ == "__main__":
    mcp.run()