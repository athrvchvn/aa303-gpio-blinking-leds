"""
Experiment 5, Part A - BMP280 pressure, temperature and altitude on the Raspberry Pi.

The BMP280 breakout is read over I2C (bus 1: SDA = GPIO2 / pin 3, SCL = GPIO3 /
pin 5) at address 0x76 with the adafruit_bmp280 library. Every second the
program prints the temperature, the pressure and the altitude computed from
the pressure against the standard sea-level reference of 1013.25 hPa.

Wiring (module pin -> Raspberry Pi header):
    VCC -> pin 1, 3.3 V        SDA -> pin 3, GPIO2
    GND -> pin 6, GND          SCL -> pin 5, GPIO3
    (CSB and SDO left unconnected: I2C mode, address 0x76)

Setup:   sudo raspi-config  ->  Interface Options -> I2C -> Enable
         sudo apt install i2c-tools && i2cdetect -y 1     (shows 0x76)
         pip3 install adafruit-circuitpython-bmp280
Run:     python3 pressure.py      (Ctrl+C to stop)
"""

import time
import board
import busio
import adafruit_bmp280

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)

# BMP280 sensor
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(
    i2c,
    address=0x76
)

# Reference pressure at your starting location
# Change this if you want better altitude accuracy
bmp280.sea_level_pressure = 1013.25

while True:
    temperature = bmp280.temperature
    pressure = bmp280.pressure
    altitude = bmp280.altitude

    print("------------------------------")
    print(f"Temperature : {temperature:.2f} °C")
    print(f"Pressure    : {pressure:.2f} hPa")
    print(f"Altitude    : {altitude:.2f} m")

    time.sleep(1)
