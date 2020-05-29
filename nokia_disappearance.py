from math import ceil
import copy
n=int(input())
original=list(map(int,input().split()))
q=int(input())
queries=[]
for i in range(q):
	queries.append(list(map(int,input().split())))	

stack=[]
stack.append(original)
i=1
while i<=ceil(n/2):
	temp=copy.deepcopy(stack[-1])
	temp[2*(i-1)]=-999
	stack.append(temp)
	#print(stac,stack)
	i+=1

while i<=n:
	temp=copy.deepcopy(stack[-1])
	temp[2*(i-1)-n]=-999
	stack.append(temp)

	i+=1


for i in queries:
	t,m=i
	m-=1
	ts=t%(2*n) #in 0 - n range
	if 0<=ts<=n:
		ptr=1
		ans=stack[ts]
		ans=[i for i in ans if i!=-999]
		if m<len(ans):
			print(ans[m])
		else:
			print(-1)
	else:
		ts-=n
		temp=stack[ts]
		complement=[]
		for i in range(len(temp)):
			if temp[i]==-999:
				complement.append(original[i])
		
		
		if m<len(complement):
			print(complement[m])
		else:
			print(-1)


	
	

	
	


