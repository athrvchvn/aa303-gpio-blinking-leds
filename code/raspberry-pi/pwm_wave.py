"""
Experiment 3, Part B - a wave of brightness travelling along eight LEDs.

Eight LEDs are driven from eight software PWM channels of the Raspberry Pi.
Every 20 ms the duty cycle of each channel is recomputed: each LED fades from
0 to 100 % over 1.6 s, back to 0 over the next 1.6 s, then stays dark for
3.2 s (a 6.4 s cycle). Neighbouring LEDs start the cycle 0.8 s apart, so four
LEDs are lit at any moment and the pattern advances one LED every 0.8 s.

Wiring (BOARD numbering - PHYSICAL header positions, LED 1 first,
LED anode -> pin, all cathodes -> GND):
    LED 1 -> pin 40        LED 5 -> pin 33
    LED 2 -> pin 38        LED 6 -> pin 32
    LED 3 -> pin 36        LED 7 -> pin 31
    LED 4 -> pin 35        LED 8 -> pin 29

Run with:  python3 pwm_wave.py      (Ctrl+C to stop)
"""

import RPi.GPIO as GPIO
import time

LED_PINS = [40, 38, 36, 35, 33, 32, 31, 29]
PWM_FREQ = 200          # Hz
CYCLE    = 6.4          # s, one fade-in / fade-out / dark cycle of an LED
STAGGER  = CYCLE / 8    # 0.8 s between the start of neighbouring LEDs
TICK     = 0.02         # s between duty-cycle updates

def duty_cycle(phase):
    """Duty cycle (0-100 %) for a position in the cycle, phase in [0, 1)."""
    if phase < 0.25:                      # fade in over the first quarter
        return 100 * phase / 0.25
    if phase < 0.5:                       # fade out over the second quarter
        return 100 * (0.5 - phase) / 0.25
    return 0                              # dark for the second half

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
pwm = []
for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
    channel = GPIO.PWM(pin, PWM_FREQ)
    channel.start(0)
    pwm.append(channel)
try:
    t0 = time.time()
    while True:
        t = time.time() - t0
        for i, channel in enumerate(pwm):
            phase = ((t - i * STAGGER) / CYCLE) % 1.0
            channel.ChangeDutyCycle(duty_cycle(phase))
        time.sleep(TICK)

except KeyboardInterrupt:
    print("\nExiting program")

finally:
    for channel in pwm:
        channel.stop()
    GPIO.cleanup()
