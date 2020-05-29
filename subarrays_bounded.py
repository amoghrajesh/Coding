#A=list(map(int,input().split()))
#L=4
#R=5
#ans=0
#for i in range(len(A)):
#	m=A[i]
#	if L<=m<=R:
#		for j in range(i+1,len(A)):
#			if A[j]>m:
#				m=A[j]
#			if m<L or m>R:
#				break
#			ans+=1
#		ans+=1
#print(ans)
import math

def noPrime(n): 
    pf=[]
    while n % 2 == 0: 
        pf.append(2)
        n = n // 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            pf.append(i) 
            n = n // i 
    if n > 2: 
        pf.append(n)
    print(pf)

noPrime(84)