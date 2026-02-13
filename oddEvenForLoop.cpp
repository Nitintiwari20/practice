#include<iostream>
using namespace std;
int main(){
    int n = 4, Evensum = 0;

    for(int i = 1 ; i <= n; i++){
        if (  i % 2 == 0 ){
            Evensum += i;
        }
    }
        cout << "Evensum =" << Evensum << endl;


    // for(int i = 1; i <= n; i++){
        
    //     if(i%2 != 0){
    //         sum += i;
    //     }
    // }
    // cout << "sum of odd numbers" << sum << endl;
    
}