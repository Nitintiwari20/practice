#include<stdio.h>
void main()
{
    int arr[100]={1,2,3,5,6};
    int i=0,n=5,num=4,pos=4;
    for(i=n;i>=pos;i--){
        arr[i]=arr[i-1];
    }
    arr[pos-1]=num;
    n++;
    for(i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
}