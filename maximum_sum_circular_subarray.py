l=list(map(int,input().split()))
m=-99999

for i in range(len(l)):
	j=(i+1)%len(l)
	s=l[i]
	while j!=i:
		if s>m:
			m=s
		print(j)
		s+=l[j]
		j=(j+1)%len(l)
	if s>m:
		m=s
print(m)
	
	
		
	