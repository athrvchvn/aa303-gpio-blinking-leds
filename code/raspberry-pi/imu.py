"""
Experiment 6, Part A - MPU6050 IMU (GY-521) on the Raspberry Pi.

Reads three-axis acceleration and angular velocity over I2C (bus 1: SDA = GPIO2 /
pin 3, SCL = GPIO3 / pin 5, address 0x68) with adafruit_mpu6050, converts them to
g and deg/s, and prints them twice a second together with the magnitude |a|
(about 1 g at rest), the tilt angles derived from the accelerometer, and the
chip temperature.

Wiring (module pin -> Raspberry Pi header):
    VCC -> pin 1, 3.3 V     SDA -> pin 3, GPIO2
    GND -> pin 6, GND       SCL -> pin 5, GPIO3    (XDA, XCL, AD0, INT unconnected)

Setup:   sudo raspi-config -> Interface Options -> I2C -> Enable
         sudo apt install i2c-tools && i2cdetect -y 1     (shows 0x68)
         pip3 install adafruit-circuitpython-mpu6050
Run:     python3 imu.py      (Ctrl+C to stop)
"""

import time
import math
import board
import busio
import adafruit_mpu6050

G = 9.80665                              # m/s^2 per g

# Initialize I2C and the sensor (GY-521, AD0 low -> 0x68)
i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
mpu.accelerometer_range = adafruit_mpu6050.Range.RANGE_2_G
mpu.gyro_range = adafruit_mpu6050.GyroRange.RANGE_250_DPS

while True:
    ax, ay, az = (v / G for v in mpu.acceleration)          # g
    gx, gy, gz = (math.degrees(v) for v in mpu.gyro)        # deg/s
    mag = math.sqrt(ax*ax + ay*ay + az*az)                  # should be ~1 g at rest
    pitch = math.degrees(math.atan2(ax, math.sqrt(ay*ay + az*az)))
    roll = math.degrees(math.atan2(ay, math.sqrt(ax*ax + az*az)))

    print("------------------------------------------")
    print(f"Accel  (g)    : X {ax:6.2f}  Y {ay:6.2f}  Z {az:6.2f}   |a| {mag:4.2f}")
    print(f"Gyro   (deg/s): X {gx:7.2f} Y {gy:7.2f} Z {gz:7.2f}")
    print(f"Tilt   (deg)  : pitch {pitch:6.1f}  roll {roll:6.1f}")
    print(f"Temperature   : {mpu.temperature:.2f} C")

    time.sleep(0.5)
