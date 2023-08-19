#include<stdio.h>
#include<math.h>
int findAns(int n){
	
	long long int arr[n+1];//last index is the answer
	arr[0]=arr[1]=arr[2]=0;
	arr[3]=1;
	
	for(int i=4;i<n+1;i++){
		arr[i]=2*arr[n-1]+(long long int)pow(2,n-4)-arr[n-4];
	}
	printf("\n");
	return arr[n+1];
	
	
}
int main(){
	int n;
	scanf("%d",&n);
	int ans=findAns(n);
	printf("%ld\n",ans);
}
