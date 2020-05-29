A = [1,0,1,0,1]
S = 2
n=len(A)
ans=0
for i in range(n):
	for j in range(i,n):
		
		if sum(A[i:j+1])==S:
			ans+=1
print(ans)