"""
Experiment 3, Part A - two groups of LEDs at two fixed PWM duty cycles.

Eight LEDs are driven from eight software PWM channels of the Raspberry Pi,
all switched at 200 Hz. The first four channels are held at 100 % duty cycle
(full brightness) and the last four at 10 % (dim), so the two groups can be
compared side by side: only the duty cycle differs between them.

Wiring (BOARD numbering - PHYSICAL header positions, LED 1 first,
LED anode -> pin, all cathodes -> GND):
    LED 1 -> pin 40        LED 5 -> pin 33
    LED 2 -> pin 38        LED 6 -> pin 32
    LED 3 -> pin 36        LED 7 -> pin 31
    LED 4 -> pin 35        LED 8 -> pin 29

Run with:  python3 pwm_two_levels.py      (Ctrl+C to stop)
"""

import RPi.GPIO as GPIO
import time

# Physical (BOARD) pin numbers of the eight LEDs, LED 1 first
LED_PINS = [40, 38, 36, 35, 33, 32, 31, 29]
PWM_FREQ = 200          # switching frequency in Hz, well above flicker

DUTY_BRIGHT = 100       # LEDs 1-4: full brightness
DUTY_DIM    = 10        # LEDs 5-8: one tenth of the average current

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pwm = []
for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
    channel = GPIO.PWM(pin, PWM_FREQ)   # one software PWM channel per pin
    channel.start(0)                    # begin with the LED off
    pwm.append(channel)
try:
    for channel in pwm[:4]:
        channel.ChangeDutyCycle(DUTY_BRIGHT)
    for channel in pwm[4:]:
        channel.ChangeDutyCycle(DUTY_DIM)
    print("LEDs 1-4 at", DUTY_BRIGHT, "% | LEDs 5-8 at", DUTY_DIM, "%")

    while True:
        time.sleep(1)                   # hold the levels until Ctrl+C

except KeyboardInterrupt:
    print("\nExiting program")

finally:
    for channel in pwm:
        channel.stop()
    GPIO.cleanup()
