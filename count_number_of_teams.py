l=list(map(int,input().split()))
n=len(l)
ans=0
if n>=3:
	
	
	#every element is j of i,j,k
	for j in range(n):
		#on the left
		leftsmall=0
		leftlarge=0
		rightsmall=0
		rightlarge=0
		for i in range(0,j):
			if l[i]>l[j]:
				leftlarge+=1
			if l[i]<l[j]:
				leftsmall+=1

		for k in range(1+j,n):
			if l[k]>l[j]:
				rightlarge+=1
			if l[k]<l[j]:
				rightsmall+=1
		
		ans+=(leftsmall*rightlarge+rightsmall*leftlarge)
	print(ans)
	
	
	
	
else:
	print(ans)