l=list(map(int,input().split()))
f=int(input())
n=len(l)
maxf=0
if n==1:
	if l[0]==0:
		if f==1:
			print(True)
		else:
			print(False)
	else:
		print(False)
if l[0]==0 and l[1]==0:
	maxf+=1
if l[-1]==0 and l[-2]==0:
	maxf+=1

for i in range(1,n-1):
	if l[i]==0 and l[i-1]==0 and l[i+1]==0:
		l[i]=1
		maxf+=1
print(f<=maxf)
	
