//define variables
#include <Wire.h>
#define shiftPin A2
#define storePin A1
#define dataPin A0
#define Enable 10
#define Step 12
#define Dir 11
#define tool0A 2
#define tool0B 3
#define tool1A 4
#define tool1B 5
#define tool2A 6
#define tool2B 7
#define tool3A 8
#define tool3B 9
//#define tool4A 10
//#define tool4B 11
//#define tool5A 12
//#define tool5B 13
#define tool6A 0
#define tool6B 1
#define tool7A 2
#define tool7B 3
#define tool8A 4
#define tool8B 5
#define tool9A 6
#define tool9B 7
boolean shoot0 = false;
boolean shoot1 = false;
boolean shoot2 = false;
boolean shoot3 = false;
boolean shoot4 = false;
boolean shoot5 = false;
boolean shoot6 = false;
boolean shoot7 = false;
boolean shoot8 = false;
boolean shoot9 = false;
enum DoD0 {idle0, forwards0, backwards0};
DoD0 dod0;
enum DoD1 {idle1, forwards1, backwards1};
DoD1 dod1;
enum Pump {step1, step2};
Pump pump;
unsigned long saved_time0;
unsigned long saved_time1;
unsigned long saved_time2;
int sr_pins = 0;
int16_t message;
byte a, b;

//L298N pins to output, i2c, serial, shift register pins to output
void setup() {
  Wire.begin(9);
  Wire.onReceive(receiveEvent);
  Serial.begin(9600);
  pinMode(tool0A, OUTPUT);
  pinMode(tool0B, OUTPUT);
  pinMode(tool1A, OUTPUT);
  pinMode(tool1B, OUTPUT);
  pinMode(tool2A, OUTPUT);
  pinMode(tool2B, OUTPUT);
  pinMode(tool3A, OUTPUT);
  pinMode(tool3B, OUTPUT);
  //pinMode(tool4A, OUTPUT);
  //pinMode(tool4B, OUTPUT);
  //pinMode(tool5A, OUTPUT);
  //pinMode(tool5B, OUTPUT);
  pinMode(shiftPin, OUTPUT);
  pinMode(storePin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  pinMode(Enable, OUTPUT);
  pinMode(Step, OUTPUT);
  pinMode(Dir, OUTPUT);
  digitalWrite(Enable, LOW);
  digitalWrite(Dir, LOW);
}

//read i2c message
//check which tool bit is set
void receiveEvent() {
  while (Wire.available()) {
    a = Wire.read();
    b = Wire.read();
  }
  message = a;
  message = (message << 8) | b;
  if (bitRead(message, 0) == 1 ) {
    dod1 = forwards1;
    shoot0 = true;
  }
  if (bitRead(message, 1) == 1 ) {
    dod1 = forwards1;
    shoot1 = true;
  }
  if (bitRead(message, 2) == 1 ) {
    shoot2 = true;
    dod1 = forwards1;
  }
  if (bitRead(message, 3) == 1 ) {
    shoot3 = true;
    dod1 = forwards1;
  }
  if (bitRead(message, 4) == 1 ) {
    shoot4 = true;
    dod1 = forwards1;
  }
  if (bitRead(message, 5) == 1 ) {
    shoot5 = true;
    dod1 = forwards1;
  }
  if (bitRead(message, 6) == 1 ) {
    shoot6 = true;
    dod1 = forwards1;
  }
  if (bitRead(message, 7) == 1 ) {
    shoot7 = true;
    dod1 = forwards1;
  }
  if (bitRead(message, 8) == 1 ) {
    shoot8 = true;
    dod1 = forwards1;
  }
  if (bitRead(message, 9) == 1 ) {
    shoot9 = true;
    dod1 = forwards1;
  }
  if (bitRead(message, 10) == 1 ) {
    dod0 = forwards0;
  }
  if (bitRead(message, 10) == 0 ) {
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
        //digitalWrite(tool4A, HIGH);
        //digitalWrite(tool4B, LOW);
        //digitalWrite(tool5A, HIGH);
        //digitalWrite(tool5B, LOW);
        digitalWrite(storePin, LOW);
        bitSet(sr_pins, tool6A);
        bitClear(sr_pins, tool6B);
        shiftOut(dataPin, shiftPin, MSBFIRST, sr_pins);
        digitalWrite(storePin, HIGH);
        digitalWrite(storePin, LOW);
        bitSet(sr_pins, tool7A);
        bitClear(sr_pins, tool7B);
        shiftOut(dataPin, shiftPin, MSBFIRST, sr_pins);
        digitalWrite(storePin, HIGH);
        digitalWrite(storePin, LOW);
        bitSet(sr_pins, tool8A);
        bitClear(sr_pins, tool8B);
        shiftOut(dataPin, shiftPin, MSBFIRST, sr_pins);
        digitalWrite(storePin, HIGH);
        digitalWrite(storePin, LOW);
        bitSet(sr_pins, tool9A);
        bitClear(sr_pins, tool9B);
        shiftOut(dataPin, shiftPin, MSBFIRST, sr_pins);
        digitalWrite(storePin, HIGH);
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
        //digitalWrite(tool4A, LOW);
        //digitalWrite(tool4B, HIGH);
        //digitalWrite(tool5A, LOW);
        //digitalWrite(tool5B, HIGH);
        digitalWrite(storePin, LOW);
        bitClear(sr_pins, tool6A);
        bitSet(sr_pins, tool6B);
        shiftOut(dataPin, shiftPin, MSBFIRST, sr_pins);
        digitalWrite(storePin, HIGH);
        digitalWrite(storePin, LOW);
        bitClear(sr_pins, tool7A);
        bitSet(sr_pins, tool7B);
        shiftOut(dataPin, shiftPin, MSBFIRST, sr_pins);
        digitalWrite(storePin, HIGH);
        digitalWrite(storePin, LOW);
        bitClear(sr_pins, tool8A);
        bitSet(sr_pins, tool8B);
        shiftOut(dataPin, shiftPin, MSBFIRST, sr_pins);
        digitalWrite(storePin, HIGH);
        digitalWrite(storePin, LOW);
        bitClear(sr_pins, tool9A);
        bitSet(sr_pins, tool9B);
        shiftOut(dataPin, shiftPin, MSBFIRST, sr_pins);
        digitalWrite(storePin, HIGH);
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
      shoot4 = false;
      shoot5 = false;
      shoot6 = false;
      shoot7 = false;
      shoot8 = false;
      shoot9 = false;
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
        //        if (shoot4 == true) {
        //          digitalWrite(tool4A, HIGH);
        //          digitalWrite(tool4B, LOW);
        //        }
        //        if (shoot5 == true) {
        //          digitalWrite(tool5A, HIGH);
        //          digitalWrite(tool5B, LOW);
        //       }
        if (shoot6 == true) {
          digitalWrite(storePin, LOW);
          bitSet(sr_pins, tool6A);
          bitClear(sr_pins, tool6B);
          shiftOut(dataPin, shiftPin, MSBFIRST, sr_pins);
          digitalWrite(storePin, HIGH);
        }
        if (shoot7 == true) {
          digitalWrite(storePin, LOW);
          bitSet(sr_pins, tool7A);
          bitClear(sr_pins, tool7B);
          shiftOut(dataPin, shiftPin, MSBFIRST, sr_pins);
          digitalWrite(storePin, HIGH);
        }
        if (shoot8 == true) {
          digitalWrite(storePin, LOW);
          bitSet(sr_pins, tool8A);
          bitClear(sr_pins, tool8B);
          shiftOut(dataPin, shiftPin, MSBFIRST, sr_pins);
          digitalWrite(storePin, HIGH);
        }
        if (shoot9 == true) {
          digitalWrite(storePin, LOW);
          bitSet(sr_pins, tool9A);
          bitClear(sr_pins, tool9B);
          shiftOut(dataPin, shiftPin, MSBFIRST, sr_pins);
          digitalWrite(storePin, HIGH);
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
        //        if (shoot4 == true) {
        //          digitalWrite(tool4A, LOW);
        //          digitalWrite(tool4B, HIGH);
        //        }
        //        if (shoot5 == true) {
        //          digitalWrite(tool5A, LOW);
        //          digitalWrite(tool5B, HIGH);
        //        }
        if (shoot6 == true) {
          digitalWrite(storePin, LOW);
          bitClear(sr_pins, tool6A);
          bitSet(sr_pins, tool6B);
          shiftOut(dataPin, shiftPin, MSBFIRST, sr_pins);
          digitalWrite(storePin, HIGH);
        }
        if (shoot7 == true) {
          digitalWrite(storePin, LOW);
          bitClear(sr_pins, tool7A);
          bitSet(sr_pins, tool7B);
          shiftOut(dataPin, shiftPin, MSBFIRST, sr_pins);
          digitalWrite(storePin, HIGH);
        }
        if (shoot8 == true) {
          digitalWrite(storePin, LOW);
          bitClear(sr_pins, tool8A);
          bitSet(sr_pins, tool8B);
          shiftOut(dataPin, shiftPin, MSBFIRST, sr_pins);
          digitalWrite(storePin, HIGH);
        }
        if (shoot9 == true) {
          digitalWrite(storePin, LOW);
          bitClear(sr_pins, tool9A);
          bitSet(sr_pins, tool9B);
          shiftOut(dataPin, shiftPin, MSBFIRST, sr_pins);
          digitalWrite(storePin, HIGH);
        }
      }
      else
      {
        dod1 = idle1;
      }
      break;
  }
  //run pump
  switch (pump) {
    case step1:
      if (micros() - saved_time2 < 500) {
        digitalWrite(Step, HIGH);
      }
      else
      {
        pump = step2;
      }
      break;
    case step2:
      if (micros() - saved_time2 < 1000) {
        digitalWrite(Step, LOW);
      }
      else
      {
        pump = step1;
        saved_time2 = micros();
      }
      break;
  }
}
