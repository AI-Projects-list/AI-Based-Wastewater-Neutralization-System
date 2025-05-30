void loop() {
  float ph = readPH();
  float tds = readTDS();
  float orp = readORP();
  String payload = "{"ph":" + String(ph) + ","tds":" + String(tds) + ","orp":" + String(orp) + "}";
  postToServer(payload);
  delay(5000);
}