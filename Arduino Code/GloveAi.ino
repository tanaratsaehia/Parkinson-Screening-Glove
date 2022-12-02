#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>

Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(12345);
Adafruit_ADXL345_Unified accel2 = Adafruit_ADXL345_Unified(12346);

void setup(void) {
#ifndef ESP32
  while (!Serial);
  Serial.begin(9600);
  if(!accel2.begin(0x1D)){
    Serial.println("Ooops, no ADXL345 detected ... Check your 0x1D wiring!");
    while(1);
  }
  if(!accel.begin(0x53)){
    Serial.println("Ooops, no ADXL345 detected ... Check your 0x53 wiring!");
    while(1);
  }
   accel.setRange(ADXL345_RANGE_16_G);
   accel2.setRange(ADXL345_RANGE_16_G);
}

void loop(void) {
  sensors_event_t event; 
  accel.getEvent(&event);
  Serial.print(event.acceleration.x); Serial.print("_");
  Serial.print(event.acceleration.y); Serial.print("_");
  Serial.print(event.acceleration.z); Serial.print("_");

  sensors_event_t event2; 
  accel2.getEvent(&event2);
  Serial.print(event2.acceleration.x); Serial.print("_");
  Serial.print(event2.acceleration.y); Serial.print("_");
  Serial.println(event2.acceleration.z);
  delay(10);
}
