#include <iostream>

using namespace std;

int abs_value(int value){
    return value < 0 ? -value : value;
}

void update(int *a, int *b){
    (*a) = (*a) + (*b);
    (*b) = (*a) - (*b);
}

int main(){
    int a, b;
    int *pa = &a, *pb = &b;

    cin >> a;
    cin >> b;
    update (pa, pb);
    cout << a << '\n' << abs_value(b) << endl;

    return 0;
}