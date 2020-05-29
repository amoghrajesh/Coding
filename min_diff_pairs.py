l.sort()
m=10**5
n=len(l)
for i in range(0,n-1):
	d=l[i+1]-l[i]
	if d < m:
		m=d
ans=[]
for i in range(0,n-1):
	d=l[i+1]-l[i]
	if d==m:
		ans.append([l[i],l[i+1]])
print(ans)