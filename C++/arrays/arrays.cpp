#include <iostream>
#include <limits>
//#include <ios>
using namespace std;

int main(){
	int num_elements;

	cin >> num_elements;
	int array[num_elements];

	for(int i = 0; i < num_elements; i++){
		cin >> array[i];
	}

	cin.ignore(numeric_limits<streamsize>::max(), '\n');

	for(int i = num_elements-1; i >= 0; i--){
		cout << array[i] << ' ';
	}

	return 0;
}
