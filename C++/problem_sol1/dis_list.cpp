#include <iostream>
#include <algorithm>
//#include <bits/stdc++.h>
//#include <vector>

using namespace std;

//void distinc_Elements(int a[], int i)
//{
//	for (int var1=0; var1 < i; var1++){
//		for(int var2=0; var2 < var1; var2++){

//		}
//	}
//}

void show_list(int a[]){
	for (int i = 0; i < 10; ++i){
		cout << a[i] << " ";
	}
}

void swap(int* x_, int* y_){
	int temporary = *x_;
	*x_ = *y_;
	*y_ = temporary;
}

int main(){

	int arr[10] = {6, 10, 5, 4, 9, 120, 4, 6, 10};

	//int a = 10, b = 20;
	sort(arr, arr + 10);

	//'show_list(arr);

	int tick = 1;

	for (int i = 0; i <= 9; i++){
		if (arr[i] == arr[i + 1])
		{
			++tick;
		}
		else
		{
			continue;
		}
	}

	cout << tick - 1 << endl;
	//swap(&a, &b);
	//cout << a << " " << b;

	//char c = 0xff;
	//int n  = c + 1;
	//cout << n << endl;

	//int m = 23;
	//m |= 0x100;

	//cout << m;
	return 0;
}