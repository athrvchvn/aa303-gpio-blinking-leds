# AA303 — IoT for Space Applications
## Source code — shared by Lab Reports 1 and 2

Chavan Atharva Sunil · 240003021

Source code for both lab reports, on both boards. Each file corresponds to a
listing in one or both reports:

- [`../report-1/`](../report-1/) — Basic Operations Using GPIO: Blinking LEDs
  (four LEDs blinking together, a one-LED-at-a-time chaser, and the eight-LED
  binary display)
- [`../report-2/`](../report-2/) — Binary Representation of Numbers Using LEDs
  (the eight-LED binary display in more detail, on the Raspberry Pi only)

---

### Raspberry Pi (Python, `RPi.GPIO`)

| File | Listing | What it does |
|---|---|---|
| `raspberry-pi/blink_all_leds.py` | Listing 1 | Four LEDs blink simultaneously, 1 s ON / 1 s OFF |
| `raspberry-pi/sequential_leds.py` | Listing 3 | One LED ON at a time, advancing once per second |
| `raspberry-pi/binary_leds.py` | Report 1 Listing 4 · Report 2 Listing 1 | Eight LEDs display a decimal number (0–255) in binary. Used by both reports. |

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

| Sketch | Listing | What it does |
|---|---|---|
| `esp32/blink_all_leds/` | Listing 2 | Four LEDs blink simultaneously, 1 s ON / 1 s OFF |
| `esp32/sequential_leds/` | — | One LED ON at a time (the ESP32 version described in §3.3) |
| `esp32/binary_leds/` | Report 1 Listing 5 | Eight LEDs display a number entered on the Serial Monitor. Report 2 covers the Raspberry Pi only. |

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
