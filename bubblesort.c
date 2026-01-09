#include<stdio.h>

void main()
{
    int i,j,t,a[4];
    printf("Enter an array:");
    for(i=0;i<4;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<4;i++)
    {
        for(j=0;j<4-i-1;j++)
        {
            if(a[j]>a[j+1])
            {
                t=a[j];
                a[j]=a[j+1];
                a[j+1]=t;         
            }
        }
    }
    printf("Sorted Array is:\n");
    for(i=0;i<4;i++)
        {
            printf("%d ",a[i]);
        }
    
}