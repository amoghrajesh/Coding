n=int(input())
stack=[]
while n!=0:
	x=n%2
	n=n//2
	if x==1:
		stack.append(0)
	else:
		stack.append(1)

j=0
ans=0
for i in stack:
	ans+=(i*2**j)
	j+=1
print(ans)