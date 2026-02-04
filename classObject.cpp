#include<iostream>
using namespace std;

    class Student{
        public:
            int id;//data member
            string name;//data member
            void insert(int i,string n){
                id = i;
                name=n;
                }
            void display(){
                cout <<id<<""<<name<<endl;
                }
            };
int main(){
    Student s1;
    Student s2;
    s1.insert(101,"true engineer");
    s2.insert(102,"true eng");
    s1.display();
    s2.display();
    return 0;
}
    
