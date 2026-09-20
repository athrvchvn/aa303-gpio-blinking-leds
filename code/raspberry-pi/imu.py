"""
Experiment 6, Part A - MPU6050 IMU (GY-521) on the Raspberry Pi, raw registers.

Wakes the MPU6050 and prints the raw 16-bit accelerometer and gyroscope counts
twice a second, read register by register over I2C bus 1 (SDA = GPIO2 / pin 3,
SCL = GPIO3 / pin 5, address 0x68). Default ranges: 16384 counts per g and
131 counts per deg/s, so a resting module shows |accel| ~ 16384.

Wiring (module pin -> Raspberry Pi header):
    VCC -> pin 1, 3.3 V     SDA -> pin 3, GPIO2
    GND -> pin 6, GND       SCL -> pin 5, GPIO3    (XDA, XCL, AD0, INT unconnected)

Setup:   sudo raspi-config -> Interface Options -> I2C -> Enable
         sudo apt install i2c-tools && i2cdetect -y 1     (shows 0x68)
         pip3 install smbus2
Run:     python3 imu.py      (Ctrl+C to stop)
"""

import time
from smbus2 import SMBus

MPU_ADDR   = 0x68        # GY-521 with AD0 low
PWR_MGMT_1 = 0x6B        # power management: bit 6 = sleep
ACCEL_XOUT = 0x3B        # six accelerometer bytes start here
GYRO_XOUT  = 0x43        # six gyroscope bytes start here

bus = SMBus(1)                                   # I2C bus 1: GPIO2 = SDA, GPIO3 = SCL
bus.write_byte_data(MPU_ADDR, PWR_MGMT_1, 0)     # wake the chip (it boots asleep)

def read_word(reg):
    # signed 16-bit value from a high/low register pair
    high = bus.read_byte_data(MPU_ADDR, reg)
    low = bus.read_byte_data(MPU_ADDR, reg + 1)
    value = (high << 8) | low
    return value - 65536 if value > 32767 else value

while True:
    ax = read_word(ACCEL_XOUT)                   # raw counts: 16384 per g
    ay = read_word(ACCEL_XOUT + 2)
    az = read_word(ACCEL_XOUT + 4)
    gx = read_word(GYRO_XOUT)                    # raw counts: 131 per deg/s
    gy = read_word(GYRO_XOUT + 2)
    gz = read_word(GYRO_XOUT + 4)

    print(f"Accel: X= {ax:6d}, Y= {ay:6d}, Z= {az:6d}")
    print(f"Gyro:  X= {gx:6d}, Y= {gy:6d}, Z= {gz:6d}")
    time.sleep(0.5)
