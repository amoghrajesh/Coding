n,m,k,s=list(map(int,input().split()))
matrix=[]
for i in range(n):
	temp=input().split()
	matrix.append(temp)


	
while i<n:
	j=0
	while j<m:
		if matrix[i][j]=='#':
			j=m
		else:
			if j==m-1:
				if matrix[i][j]=='.':
					s-=2
				else:
					s+=5
			else:
				if matrix[i][j]=='.':
					s-=3
				else:
					s+=4
			j+=1
	print(i,j,s)
	i+=1

				
			
	
#if s>=k:
#	print("Yes")
#else:
#	print("No")
#print(s)