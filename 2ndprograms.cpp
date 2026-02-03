#include<iostream>
using namespace std;
int main()
{
    char ch;
    cout << "enter ch:";
    cin >> ch;
    
    if(ch >= 65 && ch <= 90){
        cout << "ch is uppercase/n";
    }else {
        cout << "ch is lowercase/n";
    }

    return 0;
}
