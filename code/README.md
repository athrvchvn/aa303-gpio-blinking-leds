# AA303 — IoT for Space Applications
## Source code — shared by Lab Reports 1 to 4

Chavan Atharva Sunil · 240003021

Source code for all four lab reports. Each file corresponds to a listing in
one or more reports:

- [`../report-1/`](../report-1/) — Basic Operations Using GPIO: Blinking LEDs
  (four LEDs blinking together, a one-LED-at-a-time chaser, and the eight-LED
  binary display)
- [`../report-2/`](../report-2/) — Binary Representation of Numbers Using LEDs
  (the eight-LED binary display in more detail, on the Raspberry Pi only)
- [`../report-3/`](../report-3/) — Pulse Width Modulation Using GPIO
  (eight LEDs dimmed by software PWM, on the Raspberry Pi only)
- [`../report-4/`](../report-4/) — DHT11 Sensor Data Reading for Temperature
  and Humidity (single-wire sensor: `adafruit_dht` on the Raspberry Pi, and an
  ESP32 web page served from its own access point)

---

### Raspberry Pi (Python, `RPi.GPIO`)

| File | Listing | What it does |
|---|---|---|
| `raspberry-pi/blink_all_leds.py` | Listing 1 | Four LEDs blink simultaneously, 1 s ON / 1 s OFF |
| `raspberry-pi/sequential_leds.py` | Listing 3 | One LED ON at a time, advancing once per second |
| `raspberry-pi/binary_leds.py` | Report 1 Listing 4 · Report 2 Listing 1 | Eight LEDs display a decimal number (0–255) in binary. Used by both reports. |
| `raspberry-pi/pwm_two_levels.py` | Report 3 Listing 1 | Eight LEDs on software PWM at 200 Hz: LEDs 1–4 held at 100 % duty cycle, LEDs 5–8 at 10 % |
| `raspberry-pi/pwm_wave.py` | Report 3 Listing 2 | A wave of brightness along the eight LEDs: each fades 0 → 100 → 0 % over 3.2 s, then dark for 3.2 s, staggered 0.8 s apart |
| `raspberry-pi/dht.py` | Report 4 Listing 2 | Reads a DHT11 on GPIO2 every 2 s with `adafruit_dht` and prints temperature and humidity; failed frames are reported and retried |

Run from the terminal:

```bash
python3 blink_all_leds.py        # Ctrl+C to stop
```

**Pin numbering differs between the programs.** The two blink programs use
**BCM** numbering (`GPIO.setmode(GPIO.BCM)`) on GPIO 17, 18, 27 and 22.
The binary display and both PWM programs use **BOARD** numbering
(`GPIO.setmode(GPIO.BOARD)`), so their pin numbers are physical header
positions: 40, 38, 36, 35, 33, 32, 31 and 29 — most significant bit first for
the binary display, LED 1 first for the PWM programs. The same wiring serves
all three.

The PWM programs use `RPi.GPIO`'s software PWM (`GPIO.PWM(pin, 200)`,
`start()`, `ChangeDutyCycle()`, `stop()`), one channel per pin, so no
hardware PWM pins are needed.

`dht.py` is different from the others: it uses CircuitPython's `board`
module (BCM names, so `board.D2` is GPIO2 at physical pin 3) and the
`adafruit_dht` driver rather than `RPi.GPIO`. Install with
`sudo apt install libgpiod2` and `pip3 install adafruit-circuitpython-dht`,
and make sure I²C is disabled in `raspi-config` so GPIO2 is free.

---

### ESP32 (Arduino C++)

| Sketch | Listing | What it does |
|---|---|---|
| `esp32/blink_all_leds/` | Listing 2 | Four LEDs blink simultaneously, 1 s ON / 1 s OFF |
| `esp32/sequential_leds/` | — | One LED ON at a time (the ESP32 version described in §3.3) |
| `esp32/binary_leds/` | Report 1 Listing 5 | Eight LEDs display a number entered on the Serial Monitor. Reports 2 and 3 cover the Raspberry Pi only. |
| `esp32/dht11_web/` | Report 4 Listing 3 | Reads a DHT11 on GPIO4 and serves the values as a web page from the ESP32's own Wi-Fi access point `ESP32_DHT11` at `http://192.168.4.1` (page refreshes every 2 s) |

Each sketch sits in its own folder, as the Arduino IDE requires. Open the
`.ino`, select **ESP32 Dev Module** and the correct COM port, then upload.
For `binary_leds`, open the Serial Monitor at **115200 baud** with the line
ending set to **Newline**, then type a number from 0 to 255.

Blink pins: GPIO 2, 4, 5, 18.
Binary pins: GPIO 23, 22, 21, 19, 18, 5, 4, 2 (most significant bit first).
DHT11 web page: signal on GPIO 4; needs the "DHT sensor library" by Adafruit
from the Library Manager. After upload, open the Serial Monitor (115200 baud)
to see the network name and address, join the `ESP32_DHT11` network from a
phone and open `http://192.168.4.1`.

---

### Wiring

**DHT11 (Report 4):** the HW-481 module's `+`, `S` and `-` pins go to
pin 1 (3.3 V), pin 3 (GPIO2) and pin 6 (GND) of the Pi's header, or to 3V3,
GPIO4 and GND on the ESP32; the module carries its own 10 kΩ pull-up, so no
other parts are needed.

The LEDs are connected **directly** to the GPIO pins, with no series
resistors — each LED anode to its pin, and all cathodes to a common ground
rail on the breadboard returned to the board's GND pin. This is what was
done in the lab and it ran without damage, but for sustained use a series
resistor of roughly 220 Ω per LED is the recommended practice.

### Note on the 8-bit conversion

The bit string must be zero-padded to eight digits. Building it by repeated
division produces only as many digits as the number needs, and indexing
eight pins against that shorter list raises
`IndexError: list index out of range`. `format(number, '08b')` in Python and
the shift-and-mask loop `(number >> b) & 1` in C++ both always yield exactly
eight bits.
