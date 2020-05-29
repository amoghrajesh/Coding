s=input()
k=int(input())

if k==len(s):
	print('0')
if k==0:
	print(s)
else:
	stack=[]
	i=0
	while i<len(s):
		while k>0 and stack and stack[-1] > s[i]:
			stack.pop()
			k-=1
		
		stack.append(s[i])
		i+=1
	
	while k>0:
		stack.pop
		k-=1

	print(int(''.join(stack)))
