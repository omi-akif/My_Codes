#include <bits/stdc++.h>
using namespace std;

int delElement(int arr[], int size, int element)
{
	//search for the element in the array
	
	int i;

	for(i = 0; i < size; i++)
	{
		if (arr[i] == element)
			break;
	}

	if (i < size)
	{
		size = size - 1;
		for(int j = i; j < size; j++)
		{
			arr[j] = arr[j+1];
		}
	}

	return size;
}

int main()
{
	int arr[] = {11, 6, 4, 7, 10};
	int element;

	cin >> element;
	int size = sizeof(arr)/sizeof(arr[0]);

	int new_size = delElement(arr,size,element);

	cout << "The new array" << "\n";

	cout << "[";
	for (int i = 0; i < new_size; i++)
	{
		if (i != new_size)
			cout  << arr[i] << ",";
		else if (
			cout << arr[i];
	}

	cout << "]" << endl;
	return 0;
}
