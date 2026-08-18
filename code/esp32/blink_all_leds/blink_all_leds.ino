/*
 * Experiment 2 - Blinking four LEDs simultaneously on the ESP32.
 *
 * All four GPIO pins are driven HIGH together to turn every LED on, held
 * for one second, then driven LOW together for another second. loop() is
 * called repeatedly by the Arduino core, so the blinking continues
 * indefinitely.
 *
 * Wiring (LED anode -> GPIO pin, all cathodes -> GND):
 *     LED 1 -> GPIO 2      LED 3 -> GPIO 5
 *     LED 2 -> GPIO 4      LED 4 -> GPIO 18
 *
 * Board: ESP32 Dev Module
 */

int LED1 = 2;
int LED2 = 4;
int LED3 = 5;
int LED4 = 18;

void setup() {
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);
}

void loop() {
  // Turn all LEDs ON
  digitalWrite(LED1, HIGH);
  digitalWrite(LED2, HIGH);
  digitalWrite(LED3, HIGH);
  digitalWrite(LED4, HIGH);
  delay(1000);

  // Turn all LEDs OFF
  digitalWrite(LED1, LOW);
  digitalWrite(LED2, LOW);
  digitalWrite(LED3, LOW);
  digitalWrite(LED4, LOW);
  delay(1000);
}
