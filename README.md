# AA303 — IoT for Space Applications

Chavan Atharva Sunil · 240003021

Lab reports and source code for the AA303 laboratory course. Each report has its
own directory, named `Report N - <title>`, holding the compiled PDF, its LaTeX
source and its figures. The
code for all experiments is shared, and lives in [`code/`](code/) at the root.

## Reports

| Report | Title | Directory | PDF |
|---|---|---|---|
| 1 | Basic Operations Using GPIO: Blinking LEDs | [`Report 1 - Basic Operations Using GPIO - Blinking LEDs/`](Report%201%20-%20Basic%20Operations%20Using%20GPIO%20-%20Blinking%20LEDs/) | [`240003021_Atharva_Chavan_report1.pdf`](Report%201%20-%20Basic%20Operations%20Using%20GPIO%20-%20Blinking%20LEDs/240003021_Atharva_Chavan_report1.pdf) |
| 2 | Binary Representation of Numbers Using LEDs | [`Report 2 - Binary Representation of Numbers Using LEDs/`](Report%202%20-%20Binary%20Representation%20of%20Numbers%20Using%20LEDs/) | [`240003021_Atharva_Chavan_report2.pdf`](Report%202%20-%20Binary%20Representation%20of%20Numbers%20Using%20LEDs/240003021_Atharva_Chavan_report2.pdf) |
| 3 | Pulse Width Modulation Using GPIO | [`Report 3 - Pulse Width Modulation Using GPIO/`](Report%203%20-%20Pulse%20Width%20Modulation%20Using%20GPIO/) | [`240003021_Atharva_Chavan_report3.pdf`](Report%203%20-%20Pulse%20Width%20Modulation%20Using%20GPIO/240003021_Atharva_Chavan_report3.pdf) |
| 4 | DHT11 Sensor Data Reading for Temperature and Humidity | [`Report 4 - DHT11 Sensor Data Reading for Temperature and Humidity/`](Report%204%20-%20DHT11%20Sensor%20Data%20Reading%20for%20Temperature%20and%20Humidity/) | [`240003021_Atharva_Chavan_report4.pdf`](Report%204%20-%20DHT11%20Sensor%20Data%20Reading%20for%20Temperature%20and%20Humidity/240003021_Atharva_Chavan_report4.pdf) |
| 5 | BMP280 Sensor Data Reading for Pressure, Temperature and Altitude | [`Report 5 - BMP280 Sensor Data Reading for Pressure, Temperature and Altitude/`](Report%205%20-%20BMP280%20Sensor%20Data%20Reading%20for%20Pressure%2C%20Temperature%20and%20Altitude/) | [`240003021_Atharva_Chavan_report5.pdf`](Report%205%20-%20BMP280%20Sensor%20Data%20Reading%20for%20Pressure%2C%20Temperature%20and%20Altitude/240003021_Atharva_Chavan_report5.pdf) |

### Report 1 — Basic Operations Using GPIO: Blinking LEDs

Experiment performed 6 August 2026. Interfacing LEDs with a Raspberry Pi and an
ESP32 across three parts:

1. **Four LEDs blinking simultaneously** — all pins driven HIGH and LOW together at one-second intervals.
2. **One LED ON at a time** — a running-light pattern, the lit position advancing once per second.
3. **Eight-LED binary display** — a decimal number (0–255) entered at the terminal or Serial Monitor is shown on eight LEDs as its 8-bit binary equivalent.

| Path | Description |
|---|---|
| [`Report 1 - Basic Operations Using GPIO - Blinking LEDs/240003021_Atharva_Chavan_report1.pdf`](Report%201%20-%20Basic%20Operations%20Using%20GPIO%20-%20Blinking%20LEDs/240003021_Atharva_Chavan_report1.pdf) | The compiled report (10 pages) |
| [`Report 1 - Basic Operations Using GPIO - Blinking LEDs/gpio_led_lab_report.tex`](Report%201%20-%20Basic%20Operations%20Using%20GPIO%20-%20Blinking%20LEDs/gpio_led_lab_report.tex) | LaTeX source — builds with pdfLaTeX / Overleaf |
| [`Report 1 - Basic Operations Using GPIO - Blinking LEDs/figures/`](Report%201%20-%20Basic%20Operations%20Using%20GPIO%20-%20Blinking%20LEDs/figures/) | Photographs of the setups, consoles and LED patterns |

### Report 2 — Binary Representation of Numbers Using LEDs

Experiment performed 13 August 2026. A decimal number (0–255) entered at the
terminal is converted to 8-bit binary in software and displayed on eight LEDs
driven directly, with no series resistors, from the GPIO pins of a Raspberry
Pi — one LED per bit, most significant bit first.

| Path | Description |
|---|---|
| [`Report 2 - Binary Representation of Numbers Using LEDs/240003021_Atharva_Chavan_report2.pdf`](Report%202%20-%20Binary%20Representation%20of%20Numbers%20Using%20LEDs/240003021_Atharva_Chavan_report2.pdf) | The compiled report (6 pages) |
| [`Report 2 - Binary Representation of Numbers Using LEDs/gpio_binary_led_report.tex`](Report%202%20-%20Binary%20Representation%20of%20Numbers%20Using%20LEDs/gpio_binary_led_report.tex) | LaTeX source — builds with pdfLaTeX / Overleaf |
| [`Report 2 - Binary Representation of Numbers Using LEDs/figures/`](Report%202%20-%20Binary%20Representation%20of%20Numbers%20Using%20LEDs/figures/) | Photographs of the setup, consoles and the eight-LED display |

### Report 3 — Pulse Width Modulation Using GPIO

Experiment performed 10 September 2026. The brightness of eight LEDs is
controlled by software PWM from the GPIO pins of a Raspberry Pi (`RPi.GPIO`,
200 Hz, same wiring as Report 2). Two parts:

1. **Two fixed duty cycles** — four LEDs held at 100 % and four at 10 %, giving a bright group and a dim group driven by the same kind of signal.
2. **A travelling wave of brightness** — every channel fades 0 → 100 → 0 % over 3.2 s and then stays dark for 3.2 s, with neighbouring LEDs staggered by 0.8 s, so four LEDs are lit at any moment and the pattern advances one LED every 0.8 s.

| Path | Description |
|---|---|
| [`Report 3 - Pulse Width Modulation Using GPIO/240003021_Atharva_Chavan_report3.pdf`](Report%203%20-%20Pulse%20Width%20Modulation%20Using%20GPIO/240003021_Atharva_Chavan_report3.pdf) | The compiled report (8 pages) |
| [`Report 3 - Pulse Width Modulation Using GPIO/gpio_pwm_led_report.tex`](Report%203%20-%20Pulse%20Width%20Modulation%20Using%20GPIO/gpio_pwm_led_report.tex) | LaTeX source — builds with pdfLaTeX / Overleaf |
| [`Report 3 - Pulse Width Modulation Using GPIO/figures/`](Report%203%20-%20Pulse%20Width%20Modulation%20Using%20GPIO/figures/) | Stills taken from the demonstration videos, plus the two CSV files behind the duty-cycle charts (`pwm_wave_program.csv` is the programmed profile; `led_brightness.csv` is the brightness of each LED read off the video frames) |

### Report 4 — DHT11 Sensor Data Reading for Temperature and Humidity

A DHT11 sensor (HW-481 three-pin module) read over its single-wire interface
on two boards:

1. **Raspberry Pi 4** (10 September 2026) — `adafruit_dht` on GPIO2, printing temperature and relative humidity every two seconds; the 18 readings recorded on video (30.9 → 28.7 °C, 46 → 53 % RH) are tabulated and plotted, along with the four checksum/incomplete-frame errors the library reported and retried.
2. **ESP32** (3 September 2026) — the Adafruit DHT library on GPIO4, with the board running as a Wi-Fi access point (`ESP32_DHT11`) and serving the readings as a web page at `192.168.4.1`, viewed on a phone (26.10 °C, 55.80 %).

| Path | Description |
|---|---|
| [`Report 4 - DHT11 Sensor Data Reading for Temperature and Humidity/240003021_Atharva_Chavan_report4.pdf`](Report%204%20-%20DHT11%20Sensor%20Data%20Reading%20for%20Temperature%20and%20Humidity/240003021_Atharva_Chavan_report4.pdf) | The compiled report (8 pages) |
| [`Report 4 - DHT11 Sensor Data Reading for Temperature and Humidity/dht11_sensor_report.tex`](Report%204%20-%20DHT11%20Sensor%20Data%20Reading%20for%20Temperature%20and%20Humidity/dht11_sensor_report.tex) | LaTeX source — builds with pdfLaTeX / Overleaf |
| [`Report 4 - DHT11 Sensor Data Reading for Temperature and Humidity/figures/`](Report%204%20-%20DHT11%20Sensor%20Data%20Reading%20for%20Temperature%20and%20Humidity/figures/) | Photographs of the setups and the module, and stills (Pi terminal, phone page, Arduino IDE) taken from the demonstration videos |

### Report 5 — BMP280 Sensor Data Reading for Pressure, Temperature and Altitude

A BMP280 barometric sensor read over I²C (address 0x76) on two boards:

1. **Raspberry Pi 4** (10 September 2026) — `adafruit_bmp280` on bus 1 (GPIO2/GPIO3), printing temperature, pressure and pressure-altitude every second; the 14 readings recorded on video (≈929.3 hPa, ≈719 m, 31.4 → 30.1 °C) are tabulated and plotted.
2. **ESP32** (3 September 2026) — the Adafruit BMP280 library on GPIO21/22, with the board running as a Wi-Fi access point and serving a live dashboard at `192.168.4.1` (a JSON endpoint polled every second): ≈940.2 hPa, ≈627 m, 24.5 °C.

The report also works through why the same room reads 719 m on one day and 627 m on another (pressure altitude vs. the day's sea-level pressure).

| Path | Description |
|---|---|
| [`Report 5 - BMP280 Sensor Data Reading for Pressure, Temperature and Altitude/240003021_Atharva_Chavan_report5.pdf`](Report%205%20-%20BMP280%20Sensor%20Data%20Reading%20for%20Pressure%2C%20Temperature%20and%20Altitude/240003021_Atharva_Chavan_report5.pdf) | The compiled report (7 pages) |
| [`Report 5 - BMP280 Sensor Data Reading for Pressure, Temperature and Altitude/bmp280_sensor_report.tex`](Report%205%20-%20BMP280%20Sensor%20Data%20Reading%20for%20Pressure%2C%20Temperature%20and%20Altitude/bmp280_sensor_report.tex) | LaTeX source — builds with pdfLaTeX / Overleaf |
| [`Report 5 - BMP280 Sensor Data Reading for Pressure, Temperature and Altitude/figures/`](Report%205%20-%20BMP280%20Sensor%20Data%20Reading%20for%20Pressure%2C%20Temperature%20and%20Altitude/figures/) | Photographs of the setups and the module, and stills (Pi editor/terminal, ESP32 dashboard) taken from the demonstration videos |

## Code

[`code/`](code/) holds the source for every experiment, on both boards —
Python for the Raspberry Pi and Arduino sketches for the ESP32 (Reports 2
and 3 use the Raspberry Pi only; Reports 1, 4 and 5 use both). See
[`code/README.md`](code/README.md) for the file-by-file listing, the pin
assignments and the wiring notes.

## Video demonstration

Demonstration videos, along with the reports and the source code, are in the
shared Drive folder:

<https://drive.google.com/drive/folders/1cdR2mrryf5j0LEnQgIgYEAs-zB0Qj0jO?usp=sharing>

## Building a report

Each report builds from inside its own directory, where the LaTeX source sits
alongside its `figures/`:

```bash
cd "Report 1 - Basic Operations Using GPIO - Blinking LEDs"   # or any other report folder
pdflatex *.tex
pdflatex *.tex     # second pass resolves references
```

Or upload the `.tex` together with its `figures/` directory to Overleaf.
