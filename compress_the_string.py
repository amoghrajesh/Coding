s=input().split()
n=len(s)
if n==1:
	print(1)
else:
	i=0
	ans=0
	while i<n:
		j=i+1
		a=s[i]
		while j<n and a==s[j]:
			j+=1
		ans+=1
		if j!=(i+1):
			ans+=len(str(j-i))
		i=j
	print(ans)
		