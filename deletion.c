#include<stdio.h>
void main(){
    int arr[10]={1,2,3,7,4,5,6};
    int i=0,ele=7,size=7,j=0;
    for (i=0;i<size;i++){
        if(arr[i]==ele){
            for(j=i;j<size;j++){
                arr[j]=arr[j+1];
            }
            break;
        }
    }
    size--;
    for (i=0;i<size;i++){
        printf("%d ",arr[i]);
    }
}