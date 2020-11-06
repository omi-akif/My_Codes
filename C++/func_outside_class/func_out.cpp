#include <iostream>
using namespace std;

class Example 
{
	int num;
	public:
	Example() {
		num = 10;
	}
	void display();
};

void Example::display() 
{
	cout << "The value of num is: " << num;
}

int main()
{
	Example obj;
	obj.display();
	return 0;
}
