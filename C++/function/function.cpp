#include <iostream>
using namespace std;

int max_bt_two (int a, int b){
    return a > b ? a : b;
}

int max_of_four(int a, int b, int c, int d){
    return max_bt_two(a, b) > max_bt_two(c, d) ? max_bt_two (a, b) : max_bt_two(c, d);
}

int main(){
    int a, b, c, d;
    cin >> a;
    cin >> b;
    cin >> c;
    cin >> d;
    int max_int = max_of_four(a, b, c, d);
    cout << max_int << endl;
    return 0;
}

