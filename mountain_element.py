def mountain(a,l,r):

	while l<=r:
		mid = l + (r-l)//2
		if (mid-1>=l and mid+1<=r and a[mid]>a[mid-1] and a[mid]>a[mid+1]):
				return mid
		elif a[mid+1]>a[mid]:
			l=mid
		elif a[mid-1]>a[mid]:
			r=mid
	return -1

		
	
	

a=list(map(int,input().split()))
n=len(a)
ans=mountain(a,0,n-1)
print(ans)