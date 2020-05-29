def Prime(p):
	for i in range(2,p):
		if p%i==0:
			return False
	return True


t=int(input())
stack=[0]*(10**6)
stack[0]=stack[1]=0
stack[2]=1
for _ in range(t):
	stack=[0]*(10**6)
	stack[0]=stack[1]=0
	stack[2]=1
	p=3
	n=int(input())
	if n<=2:
		print(stack[n])
	else:
		while 1:
			if Prime(p):
				stack[p]=stack[p-1]+1
			else:
				stack[p]=stack[p-1]

			if stack[p]>=n:
				#print("yes")
				break

			p+=1
		print(p)

	