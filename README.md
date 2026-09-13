# AA303 — IoT for Space Applications

Chavan Atharva Sunil · 240003021

Lab reports and source code for the AA303 laboratory course. Each report has its
own directory holding the compiled PDF, its LaTeX source and its figures. The
code for all experiments is shared, and lives in [`code/`](code/) at the root.

## Reports

| Report | Title | Directory | PDF |
|---|---|---|---|
| 1 | Basic Operations Using GPIO: Blinking LEDs | [`report-1/`](report-1/) | [`240003021_Atharva_Chavan_report1.pdf`](report-1/240003021_Atharva_Chavan_report1.pdf) |
| 2 | Binary Representation of Numbers Using LEDs | [`report-2/`](report-2/) | [`240003021_Atharva_Chavan_report2.pdf`](report-2/240003021_Atharva_Chavan_report2.pdf) |
| 3 | Pulse Width Modulation Using GPIO | [`report-3/`](report-3/) | [`240003021_Atharva_Chavan_report3.pdf`](report-3/240003021_Atharva_Chavan_report3.pdf) |

### Report 1 — Basic Operations Using GPIO: Blinking LEDs

Experiment performed 6 August 2026. Interfacing LEDs with a Raspberry Pi and an
ESP32 across three parts:

1. **Four LEDs blinking simultaneously** — all pins driven HIGH and LOW together at one-second intervals.
2. **One LED ON at a time** — a running-light pattern, the lit position advancing once per second.
3. **Eight-LED binary display** — a decimal number (0–255) entered at the terminal or Serial Monitor is shown on eight LEDs as its 8-bit binary equivalent.

| Path | Description |
|---|---|
| [`report-1/240003021_Atharva_Chavan_report1.pdf`](report-1/240003021_Atharva_Chavan_report1.pdf) | The compiled report (10 pages) |
| [`report-1/gpio_led_lab_report.tex`](report-1/gpio_led_lab_report.tex) | LaTeX source — builds with pdfLaTeX / Overleaf |
| [`report-1/figures/`](report-1/figures/) | Photographs of the setups, consoles and LED patterns |

### Report 2 — Binary Representation of Numbers Using LEDs

Experiment performed 13 August 2026. A decimal number (0–255) entered at the
terminal is converted to 8-bit binary in software and displayed on eight LEDs
driven directly, with no series resistors, from the GPIO pins of a Raspberry
Pi — one LED per bit, most significant bit first.

| Path | Description |
|---|---|
| [`report-2/240003021_Atharva_Chavan_report2.pdf`](report-2/240003021_Atharva_Chavan_report2.pdf) | The compiled report (6 pages) |
| [`report-2/gpio_binary_led_report.tex`](report-2/gpio_binary_led_report.tex) | LaTeX source — builds with pdfLaTeX / Overleaf |
| [`report-2/figures/`](report-2/figures/) | Photographs of the setup, consoles and the eight-LED display |

### Report 3 — Pulse Width Modulation Using GPIO

Experiment performed 10 September 2026. The brightness of eight LEDs is
controlled by software PWM from the GPIO pins of a Raspberry Pi (`RPi.GPIO`,
200 Hz, same wiring as Report 2). Two parts:

1. **Two fixed duty cycles** — four LEDs held at 100 % and four at 10 %, giving a bright group and a dim group driven by the same kind of signal.
2. **A travelling wave of brightness** — every channel fades 0 → 100 → 0 % over 3.2 s and then stays dark for 3.2 s, with neighbouring LEDs staggered by 0.8 s, so four LEDs are lit at any moment and the pattern advances one LED every 0.8 s.

| Path | Description |
|---|---|
| [`report-3/240003021_Atharva_Chavan_report3.pdf`](report-3/240003021_Atharva_Chavan_report3.pdf) | The compiled report (8 pages) |
| [`report-3/gpio_pwm_led_report.tex`](report-3/gpio_pwm_led_report.tex) | LaTeX source — builds with pdfLaTeX / Overleaf |
| [`report-3/figures/`](report-3/figures/) | Stills taken from the demonstration videos, plus the two CSV files behind the duty-cycle charts (`pwm_wave_program.csv` is the programmed profile; `led_brightness.csv` is the brightness of each LED read off the video frames) |

## Code

[`code/`](code/) holds the source for every experiment, on both boards —
Python for the Raspberry Pi and Arduino sketches for the ESP32 (Reports 2
and 3 use the Raspberry Pi only). See
[`code/README.md`](code/README.md) for the file-by-file listing, the pin
assignments and the wiring notes.

## Video demonstration

Demonstration videos, along with the reports and the source code, are in the
shared Drive folder:

<https://drive.google.com/drive/folders/1LhoB_Ec-UeLj2YO6Qbc27we5VWibq4Kw?usp=sharing>

## Building a report

Each report builds from inside its own directory, where the LaTeX source sits
alongside its `figures/`:

```bash
cd report-1   # or report-2, report-3
pdflatex *.tex
pdflatex *.tex     # second pass resolves references
```

Or upload the `.tex` together with its `figures/` directory to Overleaf.
