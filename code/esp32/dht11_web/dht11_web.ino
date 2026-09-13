/*
 * Experiment 4, Part B - DHT11 temperature and humidity served as a web page
 * from an ESP32 running as a Wi-Fi access point.
 *
 * The ESP32 creates the network "ESP32_DHT11" and answers HTTP requests on
 * http://192.168.4.1 with a small page showing the latest DHT11 reading; the
 * page reloads itself every 2 s. A failed frame (readTemperature() returns
 * NaN) is shown as "Sensor Error!".
 *
 * Wiring (module pin -> ESP32):  + (VCC) -> 3V3,  S (signal) -> GPIO4,  - (GND) -> GND
 * Libraries: "DHT sensor library" by Adafruit (Library Manager); WiFi.h and
 * WebServer.h come with the ESP32 board package. Board: ESP32 Dev Module.
 */

#include <WiFi.h>
#include <WebServer.h>
#include <DHT.h>

#define DHTPIN  4                       // DHT11 signal pin
#define DHTTYPE DHT11

const char *AP_SSID = "ESP32_DHT11";    // the ESP32 creates this Wi-Fi network
const char *AP_PASS = "12345678";

DHT dht(DHTPIN, DHTTYPE);
WebServer server(80);

void handleRoot() {                     // called for every request of "/"
  float temperature = dht.readTemperature();   // degrees Celsius, NaN on a bad frame
  float humidity = dht.readHumidity();         // percent

  String html = "<!DOCTYPE html><html><head><meta charset='utf-8'>";
  html += "<meta http-equiv='refresh' content='2'>";       // reload every 2 s
  html += "<title>ESP32 DHT11</title></head><body>";
  html += "<h1>ESP32 DHT11 Sensor</h1>";

  if (isnan(temperature) || isnan(humidity)) {
    html += "<h2>Sensor Error!</h2>";
  }
  else {
    html += "<h2>Temperature: ";
    html += String(temperature);
    html += " &deg;C</h2>";

    html += "<h2>Humidity: ";
    html += String(humidity);
    html += " %</h2>";
  }

  html += "</body>";
  html += "</html>";

  server.send(200, "text/html", html);
}

void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.softAP(AP_SSID, AP_PASS);        // start the access point
  Serial.println("Wi-Fi started!");
  Serial.print("Network: ");            Serial.println(AP_SSID);
  Serial.print("ESP32 IP address: ");   Serial.println(WiFi.softAPIP());   // 192.168.4.1

  server.on("/", handleRoot);
  server.begin();
  Serial.println("Web server started!");
}

void loop() {
  server.handleClient();
}
