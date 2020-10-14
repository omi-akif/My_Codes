#include <ThingerESP8266.h>

#define USERNAME "omi_akif"
#define DEVICE_ID "workshop"
#define DEVICE_CREDENTIAL "F1K@4YrdW972"

#define SSID "TP-LINK_CEA6"
#define SSID_PASSWORD "123456789"

ThingerESP8266 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup() {
  pinMode(2, OUTPUT);

  thing.add_wifi(SSID, SSID_PASSWORD);

  // digital pin control example (i.e. turning on/off a light, a relay, configuring a parameter, etc)
  //thing["led"] << digitalPin(LED_BUILTIN);

  // resource output example (i.e. reading a sensor value)
  thing["millis"] >> outputValue(millis());
  thing["temperature"] >> outputValue(random(10, 100));
  thing["data"] >> outputValue(random(0, 5));

  // more details at http://docs.thinger.io/arduino/
}

void loop() {
  thing.handle();
}
