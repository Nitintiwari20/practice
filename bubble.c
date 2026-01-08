#include<stdio.h>
void main()
{
  int a[3],i,j,t;
  printf("Enter your array");
  for(i=0;i<3;i++)
   {
    scanf("%d",&a[i]);
    }

    for(i=0;i<3;i++)
    {
        for(j=0;j<3-i;j++)
        {
            if(a[j]>a[j+1])
            {
            t=a[j];
            a[j]=a[j+1];
            a[j+1]=t;
            }
        }
    }
    printf("Sorted array is\n");
    for(i=0;i<3;i++)
    {
        printf("%d ",a[i]);
    }
}