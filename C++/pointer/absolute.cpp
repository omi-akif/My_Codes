#include <iostream>

using namespace std;

int abs_value(int value){
	return value < 0 ? -value : value;
}

int main(){
	int i = 1;
	int j = 5;

	cout << abs_value(i-j) << endl;
}
