"""
Experiment 1, pattern 2 - one LED ON at a time on the Raspberry Pi.

Exactly one LED is lit at any instant. The lit position walks along the pin
list once per second, producing a running-light ("chaser") effect:
    LED 1 -> LED 2 -> LED 3 -> LED 4 -> back to LED 1

Wiring is identical to blink_all_leds.py.

Run with:  python3 sequential_leds.py      (Ctrl+C to stop)
"""

import RPi.GPIO as GPIO
import time

LED_PINS = [17, 18, 27, 22]      # BCM channel numbers

GPIO.setmode(GPIO.BCM)
for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        for on_pin in LED_PINS:                  # walk the lit position along the list
            for pin in LED_PINS:
                GPIO.output(pin, GPIO.HIGH if pin == on_pin else GPIO.LOW)
            time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
