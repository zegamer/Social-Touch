int fsrPin = 0;
int fsrReading;

void setup() {
  Serial.begin(115200);
}

void loop() {
  fsrReading = analogRead(fsrPin);
  Serial.println(fsrReading);
  if (fsrReading > 750)
    Serial.println(3);
  else if (fsrReading > 500)
    Serial.println(2);
  else if (fsrReading > 250)
    Serial.println(1);
  else
    Serial.println(0);
}
