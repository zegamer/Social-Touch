// Recieves haptic input from the mannequin arm

int fsrPin = 0;
int fsrReading;

void setup() {
  Serial.begin(115200);
}

void loop() {
  fsrReading = analogRead(A0);
  if (fsrReading > 666)
    Serial.println(2);
  else if (fsrReading > 333)
    Serial.println(1);
  else
    Serial.println(0);
  delay(10);
}
