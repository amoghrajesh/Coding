n=int(input())
ans=[]
for i in range(0,2**n):
	b=bin(i)[2:].zfill(n)
	
#	b is the current operand
	c=b[0]
	#n is bs length
	for j in range(1,n):
		c+=str(int(b[j])^int(b[j-1]))
	ans.append(c)

ans2=[]
for i in ans:
	ans2.append(int(i,2))
	
print(ans2)