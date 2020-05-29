#include<stdio.h>
int main(){

    int t,i,j,k;
    scanf("%d",&t);
    for(i=0;i<t;i++){
        int a,b;
        scanf("%d %d",&a,&b);
        for(j=a;j<=b;j++){
            for(k=2;k<j;k++){
                if(j%k==0){
                    break;
                }
                else{
                    printf("%d\n",j);
                }
            }
        }
        
    }
    return 0;
}

			