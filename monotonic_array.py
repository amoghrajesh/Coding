A=list(map(int,input().split()))
b1=1
b2=1

for i in range(len(A)-1):
	for j in range(i+1,len(A)):
		if A[j]<A[i]:
			b1=0
for i in range(len(A)-1):
	for j in range(i+1,len(A)):
		if A[j]>A[i]:
			b2=0	

if b1==0 and b2==0:
	print(False)
else:
	print(True)