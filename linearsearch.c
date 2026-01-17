#include<stdio.h>

void main()
{
    int a[5],i,n,t=0;
    printf("Enter your array");
    for(i=0;i<5;i++){
        scanf("%d",&a[i]);
    }
    printf("Enter no");
    scanf("%d",&n);
    for(i=0;i<5;i++){
        if(n==a[i]){
            t=1;
            break;
        }
    }
    if(t==1){
        printf("Element found at %d",i+1);
    }
    else{
        printf("Element not found");
    }
}