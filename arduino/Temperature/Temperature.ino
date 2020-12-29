#include "DHT.h"
#include <LiquidCrystal.h>
#include "SPI.h"
#include "RF24.h"
#include "BTLE.h"

#define DHTPIN 8
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
RF24 radio(9,10);

BTLE btle(&radio);

#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321



DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  Serial.println(F("DHTxx test!"));

  dht.begin();

  lcd.begin(16, 2);

while (!Serial) { }

Serial.println("BTLE advertisement sender");

btle.begin("Temperature");
}

void loop() {
  // Wait a few seconds between measurements.
  delay(1000);

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C "));
  Serial.print(f);
  Serial.print(F("°F  Heat index: "));
  Serial.print(hic);
  Serial.print(F("°C "));
  Serial.print(hif);
  Serial.println(F("°F"));

  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print(F("Humidity: "));
  lcd.print(h);
  lcd.setCursor(0,1);
  lcd.print(F("C Temp: "));
  lcd.print(t);

  float temp=30;

nrf_service_data buf;

//buf.service_uuid = NRF_DEVICE_INFORMATION_SERVICE_UUID; //0x180A

buf.service_uuid = NRF_TEMPERATURE_SERVICE_UUID; //0x1809

//buf.service_uuid =NRF_BATTERY_SERVICE_UUID; //0x180F

buf.value = BTLE::to_nRF_Float(temp);

btle.advertise(0x16, &buf, sizeof(buf));

//btle.advertise(0,0);

btle.hopChannel();

Serial.print(".");
  
}
