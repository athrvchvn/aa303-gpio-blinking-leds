"""
Experiment 1 - Blinking four LEDs simultaneously on the Raspberry Pi.

All four GPIO pins are set HIGH together to turn every LED on, held for one
second, then set LOW together to turn every LED off for another second.

Wiring (BCM numbering, LED anode -> GPIO pin, all cathodes -> GND):
    LED 1 -> GPIO 17 (physical pin 11)
    LED 2 -> GPIO 18 (physical pin 12)
    LED 3 -> GPIO 27 (physical pin 13)
    LED 4 -> GPIO 22 (physical pin 15)

Run with:  python3 blink_all_leds.py      (Ctrl+C to stop)
"""

import RPi.GPIO as GPIO
import time

LED_PINS = [17, 18, 27, 22]      # BCM channel numbers

GPIO.setmode(GPIO.BCM)           # use Broadcom pin numbering
for pin in LED_PINS:             # configure every pin as a digital output
    GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        # Turn all LEDs ON
        for pin in LED_PINS:
            GPIO.output(pin, GPIO.HIGH)
        time.sleep(1)

        # Turn all LEDs OFF
        for pin in LED_PINS:
            GPIO.output(pin, GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()               # reset all pins to a safe state on exit
