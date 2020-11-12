#include <iostream>

using namespace std;

int main(){
    unsigned int n, q; // Entries for number of variable length of arrays and the number of queries respectively
    unsigned int k;
    unsigned int i, j;
    cin >> n; //enter number of variable-length arrays
    cin >> q; //enter the number of queries
    

    //Created my first two dimensional array

    int **a = new int *[n]; //point to an array of arrays 


    for(int x = 0; x < n; x++){  // Initialize 'x' for x is the numer of entries for a[]
        cin >> k; // Enter the number of entries
        a[x] = new int [k];
        for(int l = 0; l < k; l++){ //Iniatialize 'l' for l is the number of a[x]
            cin >> a[x][l];    
        }
    }

    int *temp = new int [q]; //temporary array

    for(int x = 0; x < q; x++){ // Inserting number of queries
        cin >> i;
        cin >> j;
        temp[x] = a[i][j];
    }
    
    
    for(int x = 0; x < q; x++){
        cout << temp[x] << endl; //Outputting number of queries.
    }

    return 0;
}