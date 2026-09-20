/*
 * Experiment 6, Part B - MPU6050 IMU readings served as a live web dashboard from
 * an ESP32 running as a Wi-Fi access point.
 *
 * The ESP32 reads the GY-521 (MPU6050) over I2C (SDA = GPIO21, SCL = GPIO22,
 * address 0x68) with the Adafruit MPU6050 library, creates the network
 * "ESP32-IMU" and serves http://192.168.4.1: "/" is the "ESP32 IMU Dashboard"
 * page and "/data" returns {ax,ay,az (g), gx,gy,gz (deg/s), t (degC)} as JSON,
 * which the page fetches five times a second.
 *
 * Wiring (module pin -> ESP32): VCC -> 3V3, GND -> GND, SDA -> GPIO21, SCL -> GPIO22
 * Libraries: "Adafruit MPU6050" (+ Adafruit Unified Sensor, Adafruit BusIO);
 * WiFi.h and WebServer.h come with the ESP32 core. Board: ESP32 Dev Module.
 */

#include <WiFi.h>
#include <WebServer.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

const char *AP_SSID = "ESP32-IMU";        // the ESP32 creates this Wi-Fi network
const char *AP_PASS = "12345678";
const float G = 9.80665;                  // m/s^2 per g

Adafruit_MPU6050 mpu;                     // I2C, default pins SDA = 21, SCL = 22
WebServer server(80);

// The dashboard page. Its script asks the ESP32 for fresh values 5 times a second.
const char PAGE[] PROGMEM = R"html(
<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ESP32 IMU Dashboard</title>
<style>
 body{font-family:sans-serif;background:#1c2738;color:#ddd;margin:16px}
 h2{font-size:15px;margin:14px 0 6px} .row{display:flex;gap:10px}
 .card{flex:1;background:#2b3a50;border-radius:10px;padding:8px;text-align:center}
 .l{font-size:12px;color:#aaa} .v{font-size:26px;font-weight:bold}
 .a .v{color:#4fc3f7} .g .v{color:#b39ddb} .t .v{color:#ff9800}
</style></head><body>
<h2>Accelerometer</h2><div class="row a">
 <div class="card"><div class="l">X Axis</div><div class="v" id="ax">--</div><div class="l">g</div></div>
 <div class="card"><div class="l">Y Axis</div><div class="v" id="ay">--</div><div class="l">g</div></div>
 <div class="card"><div class="l">Z Axis</div><div class="v" id="az">--</div><div class="l">g</div></div></div>
<h2>Gyroscope</h2><div class="row g">
 <div class="card"><div class="l">X Axis</div><div class="v" id="gx">--</div><div class="l">&deg;/s</div></div>
 <div class="card"><div class="l">Y Axis</div><div class="v" id="gy">--</div><div class="l">&deg;/s</div></div>
 <div class="card"><div class="l">Z Axis</div><div class="v" id="gz">--</div><div class="l">&deg;/s</div></div></div>
<h2>Temperature</h2><div class="row t">
 <div class="card"><div class="l">MPU6050 Temperature</div><div class="v" id="t">--</div><div class="l">&deg;C</div></div></div>
<script>
setInterval(async () => {
  const d = await (await fetch('/data')).json();
  for (const k of ['ax','ay','az','gx','gy','gz','t'])
    document.getElementById(k).textContent = d[k].toFixed(2);
}, 200);
</script></body></html>)html";

void handleRoot() { server.send_P(200, "text/html", PAGE); }

void handleData() {                       // the seven readings as one JSON object
  sensors_event_t a, g, t;
  mpu.getEvent(&a, &g, &t);               // m/s^2, rad/s, degC
  String json = "{";
  json += "\"ax\":" + String(a.acceleration.x / G, 2);
  json += ",\"ay\":" + String(a.acceleration.y / G, 2);
  json += ",\"az\":" + String(a.acceleration.z / G, 2);
  json += ",\"gx\":" + String(g.gyro.x * 180.0 / PI, 2);
  json += ",\"gy\":" + String(g.gyro.y * 180.0 / PI, 2);
  json += ",\"gz\":" + String(g.gyro.z * 180.0 / PI, 2);
  json += ",\"t\":" + String(t.temperature, 2) + "}";
  server.send(200, "application/json", json);
}

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);                              // SDA, SCL
  if (!mpu.begin(0x68)) {
    Serial.println("MPU6050 not found - check the wiring and the address");
    while (true) delay(10);
  }
  mpu.setAccelerometerRange(MPU6050_RANGE_2_G);
  mpu.setGyroRange(MPU6050_RANGE_250_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);      // on-chip low-pass filter
  WiFi.softAP(AP_SSID, AP_PASS);                   // start the access point
  Serial.print("Dashboard at http://");
  Serial.println(WiFi.softAPIP());                 // 192.168.4.1
  server.on("/", handleRoot);
  server.on("/data", handleData);
  server.begin();
}

void loop() { server.handleClient(); }
