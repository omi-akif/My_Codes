String m;

void setup() {
  // put your setup code here, to run once:
  m = 'Hello World';
  
  Serial.begin(115200);
  pinMode(2,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(m);
  delay(2000); //2 milisecond
}
