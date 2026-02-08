#include<iostream>
using namespace std;
int main(){
    int i,n,a=1;
    cout<< "Enter a number :";
    cin >> n;
    for(i=n;i>=1;i--){
         a *= i;
    }
    cout << "factorial of the number is :"<< a <<endl;









    // int i ,n = 10 , sum = 0;

    // for(i=1; i<=n; i++){

    //     if (i % 3 == 0){
    //         sum += i;
    //     }
    // }
    // cout << "sum of number:"<< sum <<endl;
}