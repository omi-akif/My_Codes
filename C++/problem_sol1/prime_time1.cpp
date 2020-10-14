#include <iostream>

using namespace std;


int main(){
    int i = 43;

    bool p1 = (i-1)%6;
    bool p2 = (i+1)%6;

    if (p1 * p1 == 0){
        cout << "True";
    }
    else{
        cout << "False";
    }
    return 0;
}