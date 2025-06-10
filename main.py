import adafruit_dht
import time

from board import D14


def main():
    dht_device = adafruit_dht.DHT11(D14)

    while True:
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        print(f"Temperature: {temperature} C, Humidity: {humidity} %")

        time.sleep(5)


if __name__ == "__main__":
    main()
