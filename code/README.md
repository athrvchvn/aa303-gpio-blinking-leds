# AA303 — IoT for Space Applications
## Source code — shared by Lab Reports 1 to 6

Chavan Atharva Sunil · 240003021

Source code for all six lab reports. Each file corresponds to a listing in
one or more reports:

- [`../Report 1 - Basic Operations Using GPIO - Blinking LEDs/`](../Report%201%20-%20Basic%20Operations%20Using%20GPIO%20-%20Blinking%20LEDs/) — Basic Operations Using GPIO: Blinking LEDs
  (four LEDs blinking together, a one-LED-at-a-time chaser, and the eight-LED
  binary display)
- [`../Report 2 - Binary Representation of Numbers Using LEDs/`](../Report%202%20-%20Binary%20Representation%20of%20Numbers%20Using%20LEDs/) — Binary Representation of Numbers Using LEDs
  (the eight-LED binary display in more detail, on the Raspberry Pi only)
- [`../Report 3 - Pulse Width Modulation Using GPIO/`](../Report%203%20-%20Pulse%20Width%20Modulation%20Using%20GPIO/) — Pulse Width Modulation Using GPIO
  (eight LEDs dimmed by software PWM, on the Raspberry Pi only)
- [`../Report 4 - DHT11 Sensor Data Reading for Temperature and Humidity/`](../Report%204%20-%20DHT11%20Sensor%20Data%20Reading%20for%20Temperature%20and%20Humidity/) — DHT11 Sensor Data Reading for Temperature
  and Humidity (single-wire sensor: `adafruit_dht` on the Raspberry Pi, and an
  ESP32 web page served from its own access point)
- [`../Report 5 - BMP280 Sensor Data Reading for Pressure, Temperature and Altitude/`](../Report%205%20-%20BMP280%20Sensor%20Data%20Reading%20for%20Pressure%2C%20Temperature%20and%20Altitude/) — BMP280 Sensor Data Reading for Pressure,
  Temperature and Altitude (I²C sensor: `adafruit_bmp280` on the Raspberry Pi,
  and a live ESP32 web dashboard served from its own access point)
- [`../Report 6 - IMU Sensor Data Reading for Inertial Navigation/`](../Report%206%20-%20IMU%20Sensor%20Data%20Reading%20for%20Inertial%20Navigation/) — IMU Sensor Data Reading for Inertial Navigation
  (MPU6050 over I²C: `adafruit_mpu6050` on the Raspberry Pi, and a live ESP32
  dashboard of acceleration and angular velocity)

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
| `raspberry-pi/pressure.py` | Report 5 Listing 2 | Reads a BMP280 over I²C (0x76) every second with `adafruit_bmp280` and prints temperature, pressure and altitude (sea-level reference 1013.25 hPa) |
| `raspberry-pi/imu.py` | Report 6 Listing 2 | Wakes the MPU6050 and prints its raw 16-bit accelerometer and gyroscope counts twice a second, read register by register with `smbus2` (16384 counts/g, 131 counts per °/s) |

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

`pressure.py` also uses CircuitPython (`board`, `busio`) with the
`adafruit_bmp280` driver over I²C. Here I²C must be **enabled** in
`raspi-config` (the opposite of `dht.py`, since the BMP280 uses GPIO2/GPIO3
as SDA/SCL); `i2cdetect -y 1` should show the sensor at `0x76`. Install with
`pip3 install adafruit-circuitpython-bmp280`.

---

### ESP32 (Arduino C++)

| Sketch | Listing | What it does |
|---|---|---|
| `esp32/blink_all_leds/` | Listing 2 | Four LEDs blink simultaneously, 1 s ON / 1 s OFF |
| `esp32/sequential_leds/` | — | One LED ON at a time (the ESP32 version described in §3.3) |
| `esp32/binary_leds/` | Report 1 Listing 5 | Eight LEDs display a number entered on the Serial Monitor. Reports 2 and 3 cover the Raspberry Pi only. |
| `esp32/dht11_web/` | Report 4 Listing 3 | Reads a DHT11 on GPIO4 and serves the values as a web page from the ESP32's own Wi-Fi access point `ESP32_DHT11` at `http://192.168.4.1` (page refreshes every 2 s) |
| `esp32/bmp280_web_dashboard/` | Report 5 Listing 3 | Reads a BMP280 over I²C and serves a live dashboard from the access point `ESP32-Sensor` at `http://192.168.4.1`; `/data` returns JSON polled every second |
| `esp32/mpu6050_web_dashboard/` | Report 6 Listing 3 | Reads an MPU6050 over I²C and serves the "ESP32 IMU Dashboard" from the access point `ESP32-IMU` at `http://192.168.4.1`; `/data` returns JSON polled 5× per second |

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
BMP280 dashboard: SDA on GPIO 21, SCL on GPIO 22; needs the "Adafruit BMP280
Library" (with Adafruit Unified Sensor and BusIO). Join the `ESP32-Sensor`
network and open `http://192.168.4.1`.

---

### Wiring

**MPU6050 / GY-521 (Report 6):** VCC, GND, SDA and SCL exactly as for the
BMP280 below (same I²C pins on both boards); XDA, XCL, AD0 and INT are left
unconnected, giving address 0x68. `imu.py` needs
`pip3 install smbus2`; the sketch needs the "Adafruit MPU6050" library.

**BMP280 (Report 5):** the six-pin breakout's VCC, GND, SDA and SCL go to
pin 1 (3.3 V), pin 6 (GND), pin 3 (GPIO2) and pin 5 (GPIO3) of the Pi's
header, or to 3V3, GND, GPIO21 and GPIO22 on the ESP32; CSB and SDO are left
unconnected (I²C mode, address 0x76). The pull-ups are on the module.

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
