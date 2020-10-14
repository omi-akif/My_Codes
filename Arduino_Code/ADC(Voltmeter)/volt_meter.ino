#include "Plotter.h"

double x; //global variables
double y;
Plotter p; //create plotter

int analogPin = A2;
float Vin = 5.0;
double R1 = 220.0;
double R2 = 0.0;
double I2;
//int digitalPin = 12;
//int val = 0; 

void setup(){
    Serial.begin(9600);
    p.Begin(); 
    p.AddXYGraph("R2 resistance", 500,"Resistance (ohm)", x, "Current (Amphere)", y);
    //pinMode(analogPin, INPUT);
    //pinMode(digitalPin, OUTPUT);
}

void loop(){
    int sensorValue = analogRead(analogPin);
    double VoutR1  = sensorValue * (5.0 / 1023.0);
    double VoutR2 = Vin-VoutR1;
    R2 = R1 * (1/((Vin/VoutR2)-1));
    I2 = R2/VoutR2;
    x = R2;
    y = I2;
    p.Plot();
}