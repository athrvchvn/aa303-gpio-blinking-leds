/*
 * Experiment 5, Part B - BMP280 readings served as a live web dashboard from an
 * ESP32 running as a Wi-Fi access point.
 *
 * The ESP32 reads the BMP280 over I2C (SDA = GPIO21, SCL = GPIO22, address 0x76)
 * with the Adafruit BMP280 library, creates the network "ESP32-Sensor" and runs a
 * web server on http://192.168.4.1:  "/" returns the dashboard page and "/data"
 * returns {"t":..,"p":..,"a":..} as JSON, which the page fetches every second.
 *
 * Wiring (module pin -> ESP32): VCC -> 3V3, GND -> GND, SDA -> GPIO21, SCL -> GPIO22
 * Libraries: "Adafruit BMP280 Library" (+ Adafruit Unified Sensor, Adafruit BusIO)
 * from the Library Manager; WiFi.h and WebServer.h come with the ESP32 core.
 */

#include <WiFi.h>
#include <WebServer.h>
#include <Wire.h>
#include <Adafruit_BMP280.h>

const char *AP_SSID = "ESP32-Sensor";     // the ESP32 creates this Wi-Fi network
const char *AP_PASS = "12345678";
const float SEA_LEVEL_HPA = 1013.25;      // reference for the altitude calculation

Adafruit_BMP280 bmp;                      // I2C, default pins SDA = 21, SCL = 22
WebServer server(80);

// The dashboard page. Its script asks the ESP32 for fresh values once per second.
const char PAGE[] PROGMEM = R"html(
<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ESP32 Sensor</title>
<style>
 body{font-family:sans-serif;background:#1c2738;color:#ddd;text-align:center}
 h1{color:#4fc3f7} #st{color:#69e069}
 .card{background:#2b3a50;border-radius:10px;width:230px;margin:14px auto;padding:10px}
 .v{color:#69e069;font-size:30px;font-weight:bold} .u{font-size:12px;color:#aaa}
</style></head><body>
<h1>ESP32 Sensor Monitor</h1><div id="st">&#9679; ESP32 Connected</div>
<div class="card">Temperature<div class="v" id="t">--</div><div class="u">&deg;C</div></div>
<div class="card">Pressure<div class="v" id="p">--</div><div class="u">hPa</div></div>
<div class="card">Altitude<div class="v" id="a">--</div><div class="u">meters</div></div>
<script>
setInterval(async () => {
  try {
    const d = await (await fetch('/data')).json();
    t.textContent = d.t.toFixed(2);
    p.textContent = d.p.toFixed(2);
    a.textContent = d.a.toFixed(2);
    st.textContent = '\u25CF ESP32 Connected';    st.style.color = '#69e069';
  } catch (e) {
    st.textContent = '\u25CF ESP32 Disconnected'; st.style.color = '#ff7070';
  }
}, 1000);
</script></body></html>)html";

void handleRoot() { server.send_P(200, "text/html", PAGE); }

void handleData() {                       // the three readings as one JSON object
  float t = bmp.readTemperature();                 // degrees Celsius
  float p = bmp.readPressure() / 100.0F;           // Pa -> hPa
  float a = bmp.readAltitude(SEA_LEVEL_HPA);       // metres
  String json = "{\"t\":";  json += String(t, 2);
  json += ",\"p\":";        json += String(p, 2);
  json += ",\"a\":";        json += String(a, 2);  json += "}";
  server.send(200, "application/json", json);
}

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);                              // SDA, SCL
  if (!bmp.begin(0x76)) {
    Serial.println("BMP280 not found - check the wiring and the address");
    while (true) delay(10);
  }
  WiFi.softAP(AP_SSID, AP_PASS);                   // start the access point
  Serial.print("Dashboard at http://");
  Serial.println(WiFi.softAPIP());                 // 192.168.4.1
  server.on("/", handleRoot);
  server.on("/data", handleData);
  server.begin();
}

void loop() { server.handleClient(); }
