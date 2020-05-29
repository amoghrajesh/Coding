letters=input().split()
target=input()

if target>=letters[-1]:
	return letters[0]
else:
	l=0
	r=len(letters)-1
	while l<r:
		m=l+(r-l)//2
		if letters[m]>target:
			r=m
		else:
			l=m+1
	return letters[l]
