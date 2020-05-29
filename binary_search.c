#include<stdio.h>
int search(int* nums,int n,int target)
{
    
    int l=0;
    int r=n-1;
    int mid=0;
    while(l<r)
    {
        mid=l+(r-l)/2;
        printf("mid: %d, a[mid]:%d \n",mid,nums[mid]);
        if(nums[mid]==target){
            return mid;
        }
        else if(nums[mid]<target){
            l=mid+1;
        }
        else{
            r=mid-1;
        }
    }
    return -1;
    
    
}
int main()
{
    int nums[]={-1,0,3,5,9,12};
    int n=6;
    printf("%d",search(nums,n,2));
}