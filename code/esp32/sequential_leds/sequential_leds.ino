/*
 * Experiment 2, pattern 2 - one LED ON at a time on the ESP32.
 *
 * Exactly one LED is lit at any instant. The four digitalWrite() calls set
 * one pin HIGH and the remaining three LOW, then delay(1000) runs before
 * the lit position advances, giving a running-light ("chaser") effect.
 *
 * Wiring is identical to blink_all_leds.ino.
 *
 * Board: ESP32 Dev Module
 */

const int LED_PINS[4] = {2, 4, 5, 18};

int onIndex = 0;                 // which LED is currently lit

void setup() {
  for (int i = 0; i < 4; i++) {
    pinMode(LED_PINS[i], OUTPUT);
    digitalWrite(LED_PINS[i], LOW);
  }
}

void loop() {
  for (int i = 0; i < 4; i++) {
    digitalWrite(LED_PINS[i], (i == onIndex) ? HIGH : LOW);
  }
  delay(1000);

  onIndex = (onIndex + 1) % 4;   // advance, wrapping back to LED 1
}
