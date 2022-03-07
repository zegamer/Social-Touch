int motorPin1 = 13;                       // vibration motor connected to analog pin 12
int motorPin2 = 12;                       // vibration motor connected to analog pin 11
int motorPin3 = 27;                      // vibration motor connected to analog pin 10
int motorPin4 = 33;                      // vibration motor connected to analog pin 9

int intensity1 = 75;                    // Level 1 intensity of the vibration motor
int intensity2 = 150;                    // Level 2 intensity of the vibration motor
int intensity3 = 250;                    // Level 3 intensity of the vibration motor

int duration = 10;

void setup() {
  Serial.begin(115200);
}

void loop() {
  
  if (Serial.available() > 0) {
    switch (Serial.parseInt()) {
      case 1:
        Serial.println(1);
        allVibrate(duration, intensity1);
        break;
      case 2:
        Serial.println(2);
        allVibrate(duration, intensity2);
        break;
      case 3:
        Serial.println(3);
        allVibrate(duration, intensity3);
        break;
      default:
        Serial.println(0);
        allVibrate(0, 0);
    }
  }
}

void allVibrate (int duration, int intensity) {
  analogWrite(motorPin1, intensity);
  analogWrite(motorPin2, intensity);
  analogWrite(motorPin3, intensity);
  analogWrite(motorPin4, intensity);

  if (duration > 0) {
    delay(duration);

    analogWrite(motorPin1, 0);
    analogWrite(motorPin2, 0);
    analogWrite(motorPin3, 0);
    analogWrite(motorPin4, 0);
  }

}


/*
  void touch (int duration, int overlap) {

  int d1 = duration - overlap;
  int d2 = duration - 2 * overlap;

  //phase 1: motor 1 for duration-overlap time
  oneVibrating (d1, motorPin1);
  //phase 2: motor 1 & 2 for overlap time
  twoVibrating(overlap, motorPin1, motorPin2);
  //phase 3: motor 2 for duration - 2xoverlap time
  oneVibrating (d2, motorPin2);
  //phase 4: motor 2 & 3 for overlap time
  twoVibrating(overlap, motorPin2, motorPin3);
  //phase 5: motor 3 for duration - 2xoverlap time
  oneVibrating (d2, motorPin3);
  //phase 6: motor 3 & 4 for overlap time
  twoVibrating(overlap, motorPin3, motorPin4);
  //phase 7: motor 4 for for duration-overlap time
  oneVibrating (d1, motorPin4);
  }

  void startVibration(int motorPin) {
  for (int i = 0; i < intensity; i += 5) {
    analogWrite(motorPin, i);
    delay(10);
  }
  }

  void oneVibrating (int duration, int motorPin) {
  analogWrite(motorPin, intensity);
  delay(duration);
  analogWrite(motorPin, 0);
  }

  void twoVibrating (int duration, int motorPin1, int motorPin2) {
  analogWrite(motorPin1, intensity);
  analogWrite(motorPin2, intensity);
  delay(duration);
  analogWrite(motorPin1, 0);
  //analogWrite(motorPin2,0);
  }
*/
