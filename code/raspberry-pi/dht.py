"""
Experiment 4 - Reading temperature and humidity from a DHT11 on the Raspberry Pi.

The DHT11 (on an HW-481 breakout module with its own pull-up resistor) is read
over its single-wire interface with the adafruit_dht library. Every two seconds
the program prints the temperature in degrees Celsius and the relative
humidity in percent. A failed frame (bad checksum, incomplete data) raises a
RuntimeError, which is reported and simply retried on the next cycle.

Wiring (module pin -> Raspberry Pi header):
    + (VCC)    -> pin 1, 3.3 V
    S (signal) -> pin 3, GPIO2  (board.D2)
    - (GND)    -> pin 6, GND

Setup:   sudo apt install libgpiod2
         pip3 install adafruit-circuitpython-dht
Run:     python3 dht.py      (Ctrl+C to stop)
"""

import time
import board
import adafruit_dht

# HW-481 (DHT11) signal pin connected to GPIO2 = physical pin 3
dht = adafruit_dht.DHT11(board.D2)

try:
    while True:
        try:
            temperature = dht.temperature      # degrees Celsius
            humidity = dht.humidity            # percent relative humidity
            print(f"Temperature: {temperature:.1f} °C")
            print(f"Humidity:    {humidity:.1f} %")
            print("-" * 28)
        except RuntimeError as error:
            # A failed frame (bad checksum, incomplete data) is normal for
            # a DHT sensor on a non-real-time OS: report it and try again.
            print("DHT reading error:", error.args[0])
        time.sleep(2.0)                        # DHT11 needs >= 1 s between reads

except KeyboardInterrupt:
    print("\nExiting program")

finally:
    dht.exit()                                 # release the pin and the sensor
