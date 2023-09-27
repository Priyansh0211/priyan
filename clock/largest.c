#include<stdio.h>
int main(){
    int arr[]={12,25,62,95,65,35,15,12};
    int i=0;
    int a;
    int b=arr[0];
    a=sizeof(arr)/sizeof(arr[0]);
    for (i=0;i<a;i++){
        if (b<=arr[i]){
            b=arr[i];
        }
       
    }
    printf("%d",b);
    
    return 0;
}