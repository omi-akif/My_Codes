int led=6;
int brightness = 0;
int fade = 5;

void setup()
{
    pinMode(led, OUTPUT);
    Serial.begin(115200);
}

void loop()
{
    analogWrite(led, brightness);
    brightness = brightness + fade;

    if (brightness <= 0 || brightness >= 255){
        fade = -fade;
    }
    delay(30);
}
/*
void setup(){
    Serial.begin(115200);
    pinMode(LED_BUILTIN, OUTPUT);
}

/*void flash(int duration){
    digitalWrite(LED_BUILTIN, HIGH);
    delay(duration);
    digitalWrite(LED_BUILTIN, LOW);
    delay(duration);
}*/

/*void loop(){
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000);
    digitalWrite(LED_BUILTIN, LOW);
    delay(1000);
}
    /*    flash(200); flash(200); flash(200);
    delay(300);
    flash(500); flash(500); flash(500);
    delay(300);
    flash(200); flash(200); flash(200);
    delay(1000);
*/

    /*digitalWrite(LED_BUILTIN, HIGH);
    delay(1000);
    digitalWrite(LED_BUILTIN, LOW);
    delay(2000);

    digitalWrite(LED_BUILTIN,HIGH);
    delay(500);
    digitalWrite(LED_BUILTIN,LOW);
    delay(500);*/

    /*byte brightness;

    if (Serial.available()){
        brightness = Serial.read();
        digitalWrite(LED_BUILTIN, brightness);
    }*/