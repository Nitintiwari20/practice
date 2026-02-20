#include<iostream>
using namespace std;
int main(){
    // int count=1;
    // while(count <= 100){
    //     cout << count <<" ";
    //     count++;
    // }
    // cout << endl;


//     int n = 5;
//     int sum = 0;
//     int i = 1;
//     while(i <= n){
//         sum = sum + i;
//         i++;
//     }
//     cout << "sum = " << sum << endl;


    int n = 10;
    int evensum = 0;
    int i = 1;

    while( i <= n){

        if( i % 2 == 0){
            evensum += i;
        }
        i++;
    }
        cout << "evensum =" << evensum <<endl;
}