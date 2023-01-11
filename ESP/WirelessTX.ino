#include <SPI.h>
#include <Wire.h>
#include <nRF24L01p.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>

Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(12345);
Adafruit_ADXL345_Unified accel2 = Adafruit_ADXL345_Unified(12346);
nRF24L01p transmitter(2,4);//CSN,CE

void setup(){
  delay(150);
  Serial.begin(115200);
  Serial.println("Ok");
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
  SPI.begin();
  SPI.setBitOrder(MSBFIRST);
  transmitter.channel(90);
  transmitter.TXaddress("Artur");
  transmitter.init();
}


void loop(){
  sensors_event_t event; 
  sensors_event_t event2; 
  accel.getEvent(&event);
  accel2.getEvent(&event2);
  float data[6] = {float(event.acceleration.x), float(event.acceleration.y), float(event.acceleration.z), float(event2.acceleration.x), float(event2.acceleration.y), float(event2.acceleration.z)};
  transmitter.txPL(data,6);
  transmitter.send(FAST);
  for(int it = 0; it < 6; it++){
      Serial.print(data[it],6);
      if(it != 5){
        Serial.print("_");
      }else {
      Serial.println();
      }
    }
  data[6] = {};
  delay(5);
}
