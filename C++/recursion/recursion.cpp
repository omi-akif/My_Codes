#include <iostream>
#include <limits>
using namespace std;

int factorial(int n){
	if (n == 0){
		return 1;
	}
	return n * factorial(n-1);
}

int main(){

	int num;
	cin >> num;
	cin.ignore(numeric_limits<streamsize>::max(), '\n');
	cout << factorial(num) << endl;
}
