#include<stdio.h>
void main()
{
    int i,j;
    for(i=1;i<=5;i++)//rows
    {
        for(j=5;j>=i;j--)//colums
        {
           printf("*");
        }
        printf("\n"); 
    }
    
}