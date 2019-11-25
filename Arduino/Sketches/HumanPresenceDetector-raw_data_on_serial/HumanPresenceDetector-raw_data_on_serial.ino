#include <OmronD6T.h>

OmronD6T sensor;

void setup() {
  Serial.begin(9600);

}

void loop() {

  sensor.scanTemp();
  
  int x, y;
  for (y = 0; y < 4; y++){
    for (x = 0; x < 4; x++){
      Serial.print(sensor.temp[x][y]);
      Serial.print(';');
    }
  }


  // Change the multiplexer input channel and read values

  // digitalWrite(multiplexerControl, HIGH);

  // sensor.scanTemp();
  
  // for (y = 0; y < 4; y++){
  //   for (x = 0; x < 4; x++){
  //     Serial.print(sensor.temp[x][y]);
  //     Serial.print(';');
  //   }
  // }
  
  // digitalWrite(multiplexerControl, LOW);

  Serial.println();

  

  delay(100);
}