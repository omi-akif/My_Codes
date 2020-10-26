#include <bits/stdc++.h>
using namespace std;

string digits[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

int main(){
unsigned int n;

cin >> n;
cin.ignore(numeric_limits<streamsize>::max(), '\n');

if (n >= 1 && n <= 9){
	cout << digits[n-1] << endl;
}
else{
	cout << "Greater than 9" << endl;
}
}