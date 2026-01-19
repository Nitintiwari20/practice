#include<stdio.h>
void main()
{
int i,j,a[3][3],b[3][3],c[3][3];
printf("Enter first matrix");
for(i=0;i<3;i++)
{
    for(j=0;j<3;j++)
    {
        scanf("%d",&a[i][j]);
    }
}
printf("Enter second matrix");
for(i=0;i<3;i++)
{
    for(j=0;j<3;j++)
    {
        scanf("%d",&b[i][j]);
    }
}


}