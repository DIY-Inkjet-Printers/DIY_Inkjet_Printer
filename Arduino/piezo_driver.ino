//define variables
#include <Wire.h>
#define tool0A 4
#define tool0B 5
#define tool1A 6
#define tool1B 7
#define tool2A 8
#define tool2B 9
#define tool3A 10
#define tool3B 11
boolean shoot0 = false;
boolean shoot1 = false;
boolean shoot2 = false;
boolean shoot3 = false;
enum DoD0 {idle0, forwards0, backwards0};
DoD0 dod0;
enum DoD1 {idle1, forwards1, backwards1};
DoD1 dod1;
unsigned long saved_time0;
unsigned long saved_time1;
byte i2c_message;


//Start serial, start i2c, set L298N pins to output
void setup() {
  Serial.begin(9600);
  Wire.begin(9);
  Wire.onReceive(receiveEvent);
  pinMode(tool0A, OUTPUT);
  pinMode(tool0B, OUTPUT);
  pinMode(tool1A, OUTPUT);
  pinMode(tool1B, OUTPUT);
  pinMode(tool2A, OUTPUT);
  pinMode(tool2B, OUTPUT);
  pinMode(tool3A, OUTPUT);
  pinMode(tool3B, OUTPUT);
}


//read i2c message
//check which tool bit is set
void receiveEvent() {
  while (Wire.available()) {
    i2c_message = Wire.read();
  }

  if (bitRead(i2c_message, 0) == 1 ) {
    dod1 = forwards1;
    shoot0 = true;
  }
  if (bitRead(i2c_message, 1) == 1 ) {
    dod1 = forwards1;
    shoot1 = true;
  }
  if (bitRead(i2c_message, 2) == 1 ) {
    shoot2 = true;
    dod1 = forwards1;
  }
  if (bitRead(i2c_message, 3) == 1 ) {
    shoot3 = true;
    dod1 = forwards1;
  }
  if (bitRead(i2c_message, 4) == 1 ) {
    dod0 = forwards0;
  }
  if (bitRead(i2c_message, 4) == 0 ) {
    dod0 = idle0;
  }
}


//to start the printhead from printer menu
void loop() {
  switch (dod0) {
    case idle0:
      break;
    case forwards0:
      if (millis() - saved_time0 < 5) {
        digitalWrite(tool0A, HIGH);
        digitalWrite(tool0B, LOW);
        digitalWrite(tool1A, HIGH);
        digitalWrite(tool1B, LOW);
        digitalWrite(tool2A, HIGH);
        digitalWrite(tool2B, LOW);
        digitalWrite(tool3A, HIGH);
        digitalWrite(tool3B, LOW);
      }
      else {
        dod0 = backwards0;
      }
      break;
    case backwards0:
      if (millis() - saved_time0 < 100) {
        digitalWrite(tool0A, LOW);
        digitalWrite(tool0B, HIGH);
        digitalWrite(tool1A, LOW);
        digitalWrite(tool1B, HIGH);
        digitalWrite(tool2A, LOW);
        digitalWrite(tool2B, HIGH);
        digitalWrite(tool3A, LOW);
        digitalWrite(tool3B, HIGH);
      }
      else
      {
        dod0 = forwards0;
        saved_time0 = millis();
      }
      break;
  }


  // eject drop on demand
  switch (dod1) {
    case idle1:
      saved_time1 = millis();
      shoot0 = false;
      shoot1 = false;
      shoot2 = false;
      shoot3 = false;
      break;
    case forwards1:
      if (millis() - saved_time1 < 5) {
        if (shoot0 == true) {
          digitalWrite(tool0A, HIGH);
          digitalWrite(tool0B, LOW);
        }
        if (shoot1 == true) {
          digitalWrite(tool1A, HIGH);
          digitalWrite(tool1B, LOW);
        }
        if (shoot2 == true) {
          digitalWrite(tool2A, HIGH);
          digitalWrite(tool2B, LOW);
        }
        if (shoot3 == true) {
          digitalWrite(tool3A, HIGH);
          digitalWrite(tool3B, LOW);
        }
      }
      else {
        dod1 = backwards1;
      }
      break;
    case backwards1:
      if (millis() - saved_time1 < 50) {
        if (shoot0 == true) {
          digitalWrite(tool0A, LOW);
          digitalWrite(tool0B, HIGH);
        }
        if (shoot1 == true) {
          digitalWrite(tool1A, LOW);
          digitalWrite(tool1B, HIGH);
        }
        if (shoot2 == true) {
          digitalWrite(tool2A, LOW);
          digitalWrite(tool2B, HIGH);
        }
        if (shoot3 == true) {
          digitalWrite(tool3A, LOW);
          digitalWrite(tool3B, HIGH);
        }
      }
      else
      {
        dod1 = idle1;
      }
      break;
  }
}
