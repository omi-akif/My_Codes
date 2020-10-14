#include "Plotter.h"

double x;
Plotter p;

void setup(){
    p.Begin();
    p.AddTimeGraph("Some title of a graph", 10000, "Voltage", x);
}

void loop(){
    x = 10*sin(2.0*PI*(millis() / 5000.0));
    p.Plot();
}