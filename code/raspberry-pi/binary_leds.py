"""
Experiment 3 - Eight-LED binary number display on the Raspberry Pi.

Reads a decimal number (0-255) from the terminal, converts it to an 8-bit
binary string and drives one LED per bit: ON where the bit is 1, OFF where
it is 0. The row of eight LEDs therefore reads as the binary value entered.

Wiring (BOARD numbering - PHYSICAL header positions, most significant bit
first, LED anode -> pin, all cathodes -> GND):
    bit 7 (128) -> pin 40        bit 3 (8) -> pin 33
    bit 6  (64) -> pin 38        bit 2 (4) -> pin 32
    bit 5  (32) -> pin 36        bit 1 (2) -> pin 31
    bit 4  (16) -> pin 35        bit 0 (1) -> pin 29

NOTE: the bit string must be zero-padded to eight digits. Building it by
repeated division yields only as many digits as the number needs, and
indexing eight pins against that shorter list raises an IndexError.
format(number, '08b') always produces exactly eight characters.

Run with:  python3 binary_leds.py      (Ctrl+C to stop)
"""

import RPi.GPIO as GPIO

# Physical (BOARD) pin numbers, most significant bit first
LED_PINS = [40, 38, 36, 35, 33, 32, 31, 29]

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        number = int(input("Enter a number (0-255): "))
        if not 0 <= number <= 255:
            print("Out of range - please enter a value from 0 to 255.")
            continue

        bits = format(number, '08b')     # zero-padded to exactly 8 digits
        print(number, "->", bits)

        for pin, bit in zip(LED_PINS, bits):
            GPIO.output(pin, GPIO.HIGH if bit == '1' else GPIO.LOW)

except KeyboardInterrupt:
    print("\nExiting program")

finally:
    GPIO.cleanup()
