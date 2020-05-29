def bs(a,l,r,key):
	
	while l<r:
		m= l + (r-l)//2
		if a[m]==key:
			r=m
		else:
			l=m+1
	return l,a[l]
	

a=[True,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False]
n=len(a)
print(bs(a,0,n-1,False))