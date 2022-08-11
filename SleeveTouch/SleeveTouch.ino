// Activates vibration sleeve based on touch input

int motorPin1 = 13;   // Motor connected to analog pin 12
int motorPin2 = 12;   // Motor connected to analog pin 11
int motorPin3 = 27;   // Motor connected to analog pin 10
int motorPin4 = 33;   // Motor connected to analog pin 9

int intensity1 = 75;  // Level 1 intensity of the vibration motor
int intensity2 = 150; // Level 2 intensity of the vibration motor
int intensity3 = 250; // Level 3 intensity of the vibration motor

int duration = 100;

void setup() {
  Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 0) {
    switch (Serial.parseInt()) {
      case 1: allVibrate(intensity1); break;
      case 2: allVibrate(intensity2); break;
      case 3: allVibrate(intensity3); break;
      default: stopVibrate();
    }
  }
}

void allVibrate(int intensity) {
  analogWrite(motorPin1, intensity);
  analogWrite(motorPin2, intensity);
  analogWrite(motorPin3, intensity);
  analogWrite(motorPin4, intensity);
}

void stopVibrate() {
  analogWrite(motorPin1, 0);
  analogWrite(motorPin2, 0);
  analogWrite(motorPin3, 0);
  analogWrite(motorPin4, 0);
}
