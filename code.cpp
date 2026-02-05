#include<iostream>
using namespace std;
int main(){
    int n = 30,i,oddnum = 1;
    for(i=10;i<=n;i++){
        if(i % 2 != 0){ 
              oddnum = i;  
                cout << oddnum <<"  ";
        }
    }
}