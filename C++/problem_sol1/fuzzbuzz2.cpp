#include <iostream>
using namespace std;

int main(){
    for(int i = 1; (i & 0x0ff) <= 100; ++i &= 0x0ff){
        if (!((i & 0xff) % 15)){
            cout << "Fuzzbuzz";
        }
        else if(!((i & 0x0ff) % 5)){
            cout << "Fuzz";
        }
        else if(!((i & 0x0ff) % 3)){
            cout << "Buzz";
        }
        else{
            cout << i;
        }
        cout << "\n";
    }
    return 0;
}