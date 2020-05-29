def bs(a,l,r):
	while l<r:
		mid=l+(r-l)//2
		if mid%2==0:
			if a[mid]==a[mid+1]:
				l=mid+1
			else:
				r=mid
		else:
			if a[mid]==a[mid-1]:
				l=mid+1
			else:
				r=mid-1
	return l,a[l]

a=[3,3,7,7,10,11,11]
n=len(a)
print(bs(a,0,n-1))