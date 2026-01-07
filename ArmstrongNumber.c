#include<stdio.h>
void main()
{
int rem,arm=0,t,n;
    printf("enter a number");
    scanf ("%d",&n);
    t=n;
    while (n>0)
{
    rem=n%10;
    arm=(arm*10)+rem;
    n=n/10;
}
if(t==arm)
    {
        printf("number is armstrong");
    }
else
    {
     printf("number not armstrong");
    }
}