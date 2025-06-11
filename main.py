import adafruit_dht

from board import D14
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("HomeAmbience", host="0.0.0.0", port=3333)

@mcp.tool()
async def get_home_ambience(room: str) -> str:
    """Get ambience of room at home."""
    if room == "office":
        dht_device = adafruit_dht.DHT11(D14, use_pulseio=False)
        temperature = dht_device.temperature
        humidity= dht_device.humidity
        return f"Ambience of {room} is {temperature} C and {humidity} % humid"
    else:
        return f"I don't know have the ambience of the {room}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
