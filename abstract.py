import random

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("HomeAmbience", host="0.0.0.0", port=3333)

@mcp.tool()
async def get_home_ambience(room: str) -> str:
    """Get ambience of room at home."""
    if room == "office":
        temperature = random.randint(20, 45)
        humidity= random.randint(30, 70)
        return f"Ambience of {room} is {temperature} C and {humidity} % humid"
    else:
        return f"I don't know have the ambience of the {room}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
