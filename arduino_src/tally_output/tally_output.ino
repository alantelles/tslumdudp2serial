int led = 8;
char msg[18];
int buf_size = 18;
byte pins[] = {2, 4, 6, 8, 10};
int pinLen = sizeof(pins);


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  for (int i; i < pinLen; i++)
    pinMode(pins[i], OUTPUT);
}

void setState(int pin, int stat) {
  if (stat == 49)
    digitalWrite(pins[pin], HIGH);
  else
    digitalWrite(pins[pin], LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  int red = Serial.readBytes(msg, buf_size);
  int recv = msg[0] + 127;
  int stat = msg[1];
  char feed[16] = {};
  if (recv > -1) {
    for (int i = 2; i < buf_size; i++)
      feed[i-2] = msg[i];
      
    Serial.print("recv ");
    Serial.print(recv);
    Serial.print(", stat ");
    Serial.println(stat);   
    Serial.println(feed);
    setState(recv, stat); 
  }
    
  delay(1);
}
