# AA303 — IoT for Space Applications
## Lab Report 1 — Basic Operations Using GPIO: Blinking LEDs

Chavan Atharva Sunil · 240003021 · experiment performed 6 August 2026

Source code for the three parts of the experiment, on both boards.
Each file corresponds to a listing in the report.

---

### Raspberry Pi (Python, `RPi.GPIO`)

| File | Report listing | What it does |
|---|---|---|
| `raspberry-pi/blink_all_leds.py` | Listing 1 | Four LEDs blink simultaneously, 1 s ON / 1 s OFF |
| `raspberry-pi/sequential_leds.py` | Listing 3 | One LED ON at a time, advancing once per second |
| `raspberry-pi/binary_leds.py` | Listing 4 | Eight LEDs display a decimal number (0–255) in binary |

Run from the terminal:

```bash
python3 blink_all_leds.py        # Ctrl+C to stop
```

**Pin numbering differs between the programs.** The two blink programs use
**BCM** numbering (`GPIO.setmode(GPIO.BCM)`) on GPIO 17, 18, 27 and 22.
The binary display uses **BOARD** numbering (`GPIO.setmode(GPIO.BOARD)`),
so its pin numbers are physical header positions: 40, 38, 36, 35, 33, 32,
31 and 29, most significant bit first.

---

### ESP32 (Arduino C++)

| Sketch | Report listing | What it does |
|---|---|---|
| `esp32/blink_all_leds/` | Listing 2 | Four LEDs blink simultaneously, 1 s ON / 1 s OFF |
| `esp32/sequential_leds/` | — | One LED ON at a time (the ESP32 version described in §3.3) |
| `esp32/binary_leds/` | Listing 5 | Eight LEDs display a number entered on the Serial Monitor |

Each sketch sits in its own folder, as the Arduino IDE requires. Open the
`.ino`, select **ESP32 Dev Module** and the correct COM port, then upload.
For `binary_leds`, open the Serial Monitor at **115200 baud** with the line
ending set to **Newline**, then type a number from 0 to 255.

Blink pins: GPIO 2, 4, 5, 18.
Binary pins: GPIO 23, 22, 21, 19, 18, 5, 4, 2 (most significant bit first).

---

### Wiring

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
