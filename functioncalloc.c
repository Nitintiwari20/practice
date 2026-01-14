#include<stdio.h>
#include<stdlib.h>
void main()
{
int n,i,ptr,sum=0;
    printf("Enter number of elements:");
    scanf("%d",&n);
    ptr=(int*)calloc(n,sizeof(int));
    if(ptr==NULL)
    {
        printf("sorry! unable to allocate memory");
        exit(0);
    }
    printf("Enter a elements of array:");
    for(i=0;i<n;++i)
    {
        scanf("%d",&ptr+i);
    }
    printf("The elements of the array are:");
    for(i=0;i<n;++i)
    {
        printf("ptr[i]");
    }
}