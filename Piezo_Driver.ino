//define variables
#include <Wire.h>
#define tool_0 5
#define tool_1 4
#define tool_2 3
#define tool_3 2
boolean shoot_0 = false;
boolean shoot_1 = false;
boolean shoot_2 = false;
boolean shoot_3 = false;
boolean auto_shoot_0 = false;
boolean auto_shoot_1 = false;
boolean auto_shoot_2 = false;
boolean auto_shoot_3 = false;
enum Auto_Drop {on_0, off_0};
Auto_Drop auto_drop;
enum Drop_On_Demand {idle_1, on_1, off_1};
Drop_On_Demand drop_on_demand;
unsigned long saved_time_0;
unsigned long saved_time_1;
byte i2c_message;


//start serial, start i2c, set Arduino pins to output
void setup() {
  Serial.begin(9600);
  Wire.begin(9);
  Wire.onReceive(receiveEvent);
  pinMode(tool_0, OUTPUT);
  pinMode(tool_1, OUTPUT);
  pinMode(tool_2, OUTPUT);
  pinMode(tool_3, OUTPUT);
}


//read i2c message
//check which tool bit is set
void receiveEvent() {
  while (Wire.available()) {
    i2c_message = Wire.read();
  }
  if (bitRead(i2c_message, 0) == 1 ) {
    drop_on_demand = on_1;
    shoot_0 = true;
  }
  if (bitRead(i2c_message, 1) == 1 ) {
    drop_on_demand = on_1;
    shoot_1 = true;
  }
  if (bitRead(i2c_message, 2) == 1 ) {
    drop_on_demand = on_1;
    shoot_2 = true;
  }
  if (bitRead(i2c_message, 3) == 1 ) {
    drop_on_demand = on_1;
    shoot_3 = true;
  }
  if (bitRead(i2c_message, 4) == 1 ) {
    auto_shoot_0 = true;
  }
  if (bitRead(i2c_message, 5) == 1 ) {
    auto_shoot_1 = true;
  }
  if (bitRead(i2c_message, 6) == 1 ) {
    auto_shoot_2 = true;
  }
  if (bitRead(i2c_message, 7) == 1 ) {
    auto_shoot_3 = true;
  }
  if (bitRead(i2c_message, 4) == 0 ) {
    auto_shoot_0 = false;
  }
  if (bitRead(i2c_message, 5) == 0 ) {
    auto_shoot_1 = false;
  }
  if (bitRead(i2c_message, 6) == 0 ) {
    auto_shoot_2 = false;
  }
  if (bitRead(i2c_message, 7) == 0 ) {
    auto_shoot_3 = false;
  }
}


void loop() {
  //eject drops at set frequency
  switch (auto_drop) {
    case on_0:
      if (millis() - saved_time_0 < 50) {
        if (auto_shoot_0 == true) {
          digitalWrite(tool_0, HIGH);
        }
        if (auto_shoot_1 == true) {
          digitalWrite(tool_1, HIGH);
        }
        if (auto_shoot_2 == true) {
          digitalWrite(tool_2, HIGH);
        }
        if (auto_shoot_3 == true) {
          digitalWrite(tool_3, HIGH);
        }
      }
      else {
        auto_drop = off_0;
      }
      break;
    case off_0:
      if (millis() - saved_time_0 < 100) {
        if (auto_shoot_0 == true) {
          digitalWrite(tool_0, LOW);
        }
        if (auto_shoot_1 == true) {
          digitalWrite(tool_1, LOW);
        }
        if (auto_shoot_2 == true) {
          digitalWrite(tool_2, LOW);
        }
        if (auto_shoot_3 == true) {
          digitalWrite(tool_3, LOW);
        }
      }
      else
      {
        auto_drop = on_0;
        saved_time_0 = millis();
      }
      break;
  }


  // eject drop on demand
  switch (drop_on_demand) {
    case idle_1:
      saved_time_1 = millis();
      shoot_0 = false;
      shoot_1 = false;
      shoot_2 = false;
      shoot_3 = false;
      break;
    case on_1:
      if (millis() - saved_time_1 < 5) {
        if (shoot_0 == true) {
          digitalWrite(tool_0, HIGH);
        }
        if (shoot_1 == true) {
          digitalWrite(tool_1, HIGH);
        }
        if (shoot_2 == true) {
          digitalWrite(tool_2, HIGH);
        }
        if (shoot_3 == true) {
          digitalWrite(tool_3, HIGH);
        }
      }
      else {
        drop_on_demand = off_1;
      }
      break;
    case off_1:
      if (millis() - saved_time_1 < 50) {
        if (shoot_0 == true) {
          digitalWrite(tool_0, LOW);
        }
        if (shoot_1 == true) {
          digitalWrite(tool_1, LOW);
        }
        if (shoot_2 == true) {
          digitalWrite(tool_2, LOW);
        }
        if (shoot_3 == true) {
          digitalWrite(tool_3, LOW);
        }
      }
      else
      {
        drop_on_demand = idle_1;
      }
      break;
  }
}
