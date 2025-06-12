# ambience-device-mcp

## Pre-requisite

- [Blinka](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi#manual-install-3157124)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Installation

Install the required Python libraries:

```sh
uv pip install -r pyproject.toml
```

## Usage

- **On Raspberry Pi 5:**

```sh
uv run rpi5.py
  ```

- **On other systems (for testing or development):**

```sh
uv run abstract.py
```

The server will start and expose the `get_home_ambience` tool via MCP.

## Notes

- Ensure your ambience sensor (for e.g. DHT11) is connected to GPIO pin D14 if using `rpi5.py`.
