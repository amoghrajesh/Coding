n=int(input())
p=1
while p*p<=n:
	p+=1
p-=1
if p*p==n:
	print(True)
else:
	print(False)