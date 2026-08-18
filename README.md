# AA303 — IoT for Space Applications · Lab Report 1

**Basic Operations Using GPIO: Blinking LEDs**

Chavan Atharva Sunil · 240003021 · experiment performed 6 August 2026

Interfacing LEDs with a Raspberry Pi and an ESP32 across three parts:

1. **Four LEDs blinking simultaneously** — all pins driven HIGH and LOW together at one-second intervals.
2. **One LED ON at a time** — a running-light pattern, the lit position advancing once per second.
3. **Eight-LED binary display** — a decimal number (0–255) entered at the terminal or Serial Monitor is shown on eight LEDs as its 8-bit binary equivalent.

## Contents

| Path | Description |
|---|---|
| [`24003021_Atharva_chavan_report1.pdf`](24003021_Atharva_chavan_report1.pdf) | The compiled report (10 pages) |
| [`gpio_led_lab_report.tex`](gpio_led_lab_report.tex) | LaTeX source — builds with pdfLaTeX / Overleaf |
| [`figures/`](figures/) | Photographs of the setups, consoles and LED patterns |
| [`code/`](code/) | Source for all three parts, on both boards — see [`code/README.md`](code/README.md) |

## Video demonstration

Demonstration videos of all three parts on both boards, along with this report and
the source code, are in the shared Drive folder:

<https://drive.google.com/drive/folders/1T0wegsZBgEGQ7PwirSbTVWgo-MvS_5ov?usp=sharing>

## Building the report

```bash
pdflatex gpio_led_lab_report.tex
pdflatex gpio_led_lab_report.tex     # second pass resolves references
```

Or upload `gpio_led_lab_report.tex` together with `figures/` to Overleaf.
