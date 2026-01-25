#include<stdio.h>
void main()
{
    int i,j;
    for(i=5;i>=1;i--)//rows
    {
        for(j=1;j<=5-i;j++)//space
        {
            printf(" ");
        }
        for(j=1;j<=i;j++)//columns
        {
            printf("*");
        }
        printf("\n");
    }
}