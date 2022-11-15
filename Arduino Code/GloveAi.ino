#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>

/* Assign a unique ID to this sensor at the same time */
//Define 2 device ID
Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(12345);
Adafruit_ADXL345_Unified accel2 = Adafruit_ADXL345_Unified(12346);



void setup(void) 
{
#ifndef ESP32
  while (!Serial); // for Leonardo/Micro/Zero
#endif
  Serial.begin(9600);
  //Serial.println("Accelerometer Test"); Serial.println("");
  
  /* Initialise the sensor */
  if(!accel2.begin(0x1D))
  {
    /* There was a problem detecting the ADXL345 ... check your connections */
    Serial.println("Ooops, no ADXL345 detected ... Check your 0x1D wiring!");
    while(1);
  }
  if(!accel.begin(0x53))
  {
    /* There was a problem detecting the ADXL345 ... check your connections */
    Serial.println("Ooops, no ADXL345 detected ... Check your 0x53 wiring!");
    while(1);
  }

  /* Set the range to whatever is appropriate for your project */
 // accel.setRange(ADXL345_RANGE_16_G);
  // accel.setRange(ADXL345_RANGE_8_G);
  // accel.setRange(ADXL345_RANGE_4_G);
   accel.setRange(ADXL345_RANGE_16_G);
   accel2.setRange(ADXL345_RANGE_16_G);
}

void loop(void) 
{
  /* Get a new sensor event */ 
  sensors_event_t event; 
  accel.getEvent(&event);
 
  /* Display the results (acceleration is measured in m/s^2) */
  Serial.print(event.acceleration.x); Serial.print("_");
  Serial.print(event.acceleration.y); Serial.print("_");
  Serial.print(event.acceleration.z); Serial.print("_");

  sensors_event_t event2; 
  accel2.getEvent(&event2);
 
  /* Display the results (acceleration is measured in m/s^2) */
  Serial.print(event2.acceleration.x); Serial.print("_");
  Serial.print(event2.acceleration.y); Serial.print("_");
  Serial.println(event2.acceleration.z);
  delay(1000);
}
