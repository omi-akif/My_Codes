#include <iostream>
#include <limits>
using namespace std;

string digits[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

unsigned short int swap(unsigned int a, unsigned int b){
	unsigned short int temp;
	temp = a;
	a = b;
	b = temp;
	return a, b;
}

int main(){
	unsigned short int a, b;

	cin >> a >> b;

	if (a > b){
		swap(a, b);
	}

	for(unsigned short int i = a; i <= b; i++){
		 if(i >= 1 && i <= 9){
			cout << digits[i-1] << '\n';
		}
		else if(i > 9){
			if(i%2==0){
				cout << "even" << '\n';
			}
			else if(i%2==1){
				cout << "odd" << '\n';
			}
		}
		else{
			continue;
		}
	}

	return 0;
}
