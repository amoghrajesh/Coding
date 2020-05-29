#include<stdio.h>
int change(int amount, int* coins, int n){

    
	if(amount=0){
		printf("here");
		return 1;
	}
	if(amount<0||n==0){
		return 0;
	}
	int ans=0;
	//consider inclusion or removal of last coin
	int include=change(amount-coins[n],coins,n);
	int exclude=change(amount,coins,n-1);
	
	
	printf("%d",include+exclude);
	return include+exclude;
    
}
int main()
{
	
	int S[] = {1,2,5};
	int n = 3;
	int N = 5;
	int ans=change(N,S,n);
	printf("hi: %d",ans);
	
}
