#include<stdio.h>

int factorial(int n){
    if(n==0||n==1){
        return 1;
    }
    else{
        return n*factorial(n-1);
    }
}
void main(){
    int num;
    printf("Enter number to find factorial of: ");
    scanf("%d",&num);
    printf("Factorial is: %d",factorial(num));
}