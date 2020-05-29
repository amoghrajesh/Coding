#include<stdio.h>

void swap(int* a,int *b){
    int temp=*a;
    *a=*b;
    *b=temp;
}

int partition(int* a,int n){
    int i=0;
    int j=n;
    int p=a[0];
    do{
        do{
           i++; 
        }while(a[i]<p);
        do{
            j--;
        }while(a[j]>p);
        swap(&a[i],&a[j]);
    }while(i<j);
    swap(&a[i],&a[j]);
    swap(&a[0],&a[j]);
    return j;
}

int main(){
    int n;
    scanf("%d",&n);
    int a[n];
    int i;
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    int ans=partition(a,n);
    for(i=0;i<n;i++){
        printf("%d ",a[i]);
    }
}
