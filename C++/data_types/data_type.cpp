#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	int integer;
	long long_value;
	char character;
	float f_value;
	double d_value;
	
	
	scanf("%d %ld %c %f %lf", &integer, &long_value, &character, &f_value, &d_value);

	cout << '\n' << '\n';

	cout << fixed << integer << '\n' << long_value << '\n' << character << '\n' << f_value << '\n' << d_value <<  endl; 
	cout << scientific << integer << '\n' << long_value << '\n' << character << '\n' << f_value << '\n' << d_value << endl;
	
	// fixed scientific hexfloat defaultfloat
	/*int - > %d 32 Bit
	  long - > %ld 64 bit
	  char - > %c character type
	  float - > %f 32 bit real value
	  double - > %lf 64 bit real value
	*/
}
