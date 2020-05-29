s=input()
n=len(s)
#lets find all the pairs
pairs=[]
if "()" in s:
	s=''.join(s.split("()"))
n=len(s)
for i in range(n):
	if s[i]=='(':
		if len(pairs)==0:
			m=n-1
		else:
			m=pairs[-1][1]-1
		for j in range(m,i,-1):
			if s[j]==')':
				pairs.append([i,j])
				break
print(pairs)
#now keep reversing it and get rid of () later
pairs=pairs[::-1]
temp=list(s)
for i in pairs:
	start,end=i
	temp[start:end+1]=temp[start:end+1][::-1]


ans=""
for i in temp:
	if i=='(' or i==')':
		pass
	else:
		ans+=i
print(ans)
	