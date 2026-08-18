/*
 * Experiment 3 - Eight-LED binary number display on the ESP32.
 *
 * Reads a decimal number (0-255) from the Serial Monitor, converts it to
 * its 8-bit binary form and drives one LED per bit: ON where the bit is 1,
 * OFF where it is 0. The binary string is echoed back to the console so
 * the display can be checked against the computed value.
 *
 * Wiring (most significant bit first, LED anode -> GPIO pin,
 * all cathodes -> GND):
 *     bit 7 (128) -> GPIO 23      bit 3 (8) -> GPIO 18
 *     bit 6  (64) -> GPIO 22      bit 2 (4) -> GPIO 5
 *     bit 5  (32) -> GPIO 21      bit 1 (2) -> GPIO 4
 *     bit 4  (16) -> GPIO 19      bit 0 (1) -> GPIO 2
 *
 * Board: ESP32 Dev Module
 * Serial Monitor: 115200 baud, line ending set to "Newline"
 */

const int LED_PINS[8] = {23, 22, 21, 19, 18, 5, 4, 2};  // MSB first

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < 8; i++) {
    pinMode(LED_PINS[i], OUTPUT);
    digitalWrite(LED_PINS[i], LOW);
  }
  Serial.println("--- 8-Bit Binary LED Controller ---");
  Serial.println("Enter a number between 0 and 255.");
}

void loop() {
  if (Serial.available() > 0) {
    String line = Serial.readStringUntil('\n');
    line.trim();
    if (line.length() == 0) return;

    int number = line.toInt();
    if (number < 0 || number > 255) {
      Serial.println("Out of range - please enter a value from 0 to 255.");
      return;
    }

    Serial.print("Number: ");  Serial.print(number);
    Serial.print("  ->  Binary: ");

    for (int b = 7; b >= 0; b--) {
      int value = (number >> b) & 1;           // extract one bit
      digitalWrite(LED_PINS[7 - b], value);    // drive the matching LED
      Serial.print(value);
    }
    Serial.println();
  }
}
