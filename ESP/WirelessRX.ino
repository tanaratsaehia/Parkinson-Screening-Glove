  #include <SPI.h>
#include <nRF24L01p.h>

nRF24L01p receiver(2,4);//CSN,CE

void setup(){
  delay(150);
  Serial.begin(115200);
  SPI.begin();
  //SPI.setClockDivider(SPI_CLOCK_DIV2);
  SPI.setBitOrder(MSBFIRST);
  receiver.channel(90);
  receiver.RXaddress("Artur");
  receiver.init();
}

float data[6];

void loop(){ 
  if(receiver.available()){
    receiver.read();
    receiver.rxPL(data,6);
    for(int it = 0; it < 6; it++){
      Serial.print(data[it],6);
      if(it != 5){
        Serial.print("_");
      }else {
      Serial.println();
      }
    }
    
    
  }
}
