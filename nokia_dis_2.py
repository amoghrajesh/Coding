n=int(input())
l=list(map(int,input().split()))
oddel=[]
evenel=[]
for i in range(n):
	if i%2==1:
		evenel.append(l[i])
	else:
		oddel.append(l[i])

q=int(input())
for _ in range(q):
	t,m=list(map(int,input().split()))
	#get it in 0-2n range
	remainder=t%(2*n)
	if remainder==0:
		m-=1
		if m<n:
			print(l[m])
		else:
			print(-1)
	#case of empty list
	elif remainder == n:
		print(-1)
	
	else:
		lenodd=len(oddel)
		leneven=len(evenel)
		y=n-remainder
		if remainder<n:
			if y>=m:
				if remainder==lenodd:
					x=m-1
					print(evenel[x])
				elif remainder>lenodd:
					x=m-1
					print(evenel[remainder-lenodd+x])
				else:
					inzton=t%n
					if m<inzton:
						x=2*m-1
						print(l[x])
					else:
						x=m-1
						print(l[inzton+x])
			else:
				print(-1)
		else:
			inzton=remainder%n
			if m>inzton:
				print(-1)
			else:
				if inzton<=lenodd:
					x=m-1
					print(oddel[x])
				else:
					y=inzton-lenodd
					doubled=2*y
					if m<=doubled:
						x=m-1
						print(l[x])
					else:
						off=m-doubled
						print(oddel[y+off-1])
		
		
	