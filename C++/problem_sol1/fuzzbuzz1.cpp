#include <iostream>
using namespace std;

 int main()
 {
    //for (short i = 1; (i & 0x0FF) <= 100; i++ &=  
for (int i = 1; (i & 0x0FF) <= 100; ++i &= 0x0FF) {
  if(!((i & 0x0FF) % 3 && (i & 0x0FF) % 5)) {
      cout << "FuzzBuzz";
  } else if(!((i & 0x0FF) % 5)) {
      cout << "F";
  } else if (!((i & 0x0FF) % 3)) {
      cout << "Buzz";
  }
    else{
        cout << i;
    }
  cout << "\n";
}
	
    //for (int i = 1; i <= 100; ++i){
    //    cout << (!(i % 3) ? i,"Fizz" : "") << (!(i % 5) ? i , "Buzz" : ""), (i ? cout << "" : cout<< i), cout << "\n";
    //}
 }

 // #include <iostream>
 // int main(){
 // 	for(int i = 1 ; i <= 100 ; ++i)
 // 		((i%5)? ((i%3)?(cout << i) :(cout << "Fizz")): cout << ((i%3)? "Buzz": "FizzBuzz")) << endl;
 // }