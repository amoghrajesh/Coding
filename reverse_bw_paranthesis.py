s=input()
s=list(s)
n=len(s)
stack=[]
for i in range(n):
	if s[i]=='(':
		stack.append(i)
	
	if s[i]==')':
		start=stack.pop()
		end=i
		s[start:end]=s[start:end][::-1]
ans=""
for i in s:
	if i=='(' or i==')':
		pass
	else:
		ans+=i
print(ans)
		