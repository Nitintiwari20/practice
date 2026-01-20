#include<stdio.h>
void main()
{
    
    int n,s=0,r,a;
    printf("Enter a no.");
    scanf("%d",&n);
    a=n;
    while(n>0) 
    {
        r=n%10;
        s=(s*10)+r;
        n=n/10;
    }
    printf("%d\n",s);
    if(a==s)
    {
        printf("No is a palindrome");
    }
    else
    {
        printf("Not a palindrome");
    }
}