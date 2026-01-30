#include<stdio.h>
void main()
{
    int x,y,z;
    printf("enter a number");
    scanf("%d",&x);
    scanf("%d",&y);
    scanf("%d",&z);
    x=y;
    y=z;
    z=y;
    printf("%d",x);
    printf("%d",y);
    printf("%d",z);

}
