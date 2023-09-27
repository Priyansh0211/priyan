#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<unistd.h>
int main(){
    int h=0,m=0,s=0;
    for(;;){
        system("cls");
        printf("%d:%d:%d",h,m,s);
        
        s++;
        if(s==60){
            m=m+1;
            s=0;
        }
        if(m==60){
            h=h+1;
            m=0;
        }
        if(h==24){
            h=0;
            m=0;
            s=0;
        }
        sleep(1);
    }
    return 0;
}
