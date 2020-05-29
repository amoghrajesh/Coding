n=int(input())
if n==0:
	print(0)
elif n==1:
	print(1)
else:
	n-=2
	a=2
	b=3
	i=0
	if n==0:
		print(a)
	elif n==1:
		print(b)
	else:
		while i<n-1:
			c=a+b
			a=b
			b=c
			i+=1

		print(c)


