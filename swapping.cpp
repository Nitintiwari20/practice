#include<iostream>
using namespace std;
int main()
{
    int a,b,c;
    cout<<"enter any two number:\n";
    cin>>a>>b;
    cout<<"a="<<a<<endl;
    cout<<"b="<<b<<endl;
    c=a;
    a=b;
    b=c;
    cout<<"Result after swapping no:\n";
    cout<<"A="<<a<<endl;
    cout<<"B="<<b;
    cout<<"\n";
    
    return 0;
}