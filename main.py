import adafruit_dht

from board import D14
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("HomeWeather", host="0.0.0.0", port=3333)

@mcp.tool()
async def get_home_weather(room: str) -> str:
    """Get weather for room at home."""
    dht_device = adafruit_dht.DHT11(D14, use_pulseio=False)
    temperature = dht_device.temperature
    humidity= dht_device.humidity
    print(temperature, humidity)
    return f"Temperature: {temperature} degree celcius, Humidity: {humidity} %"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
