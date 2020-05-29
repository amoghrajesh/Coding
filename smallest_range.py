A=list(map(int,input().split()))
K=int(input())
A.sort()
b=A[-1]-A[0]
m=9999
for x in range(-K,K+1):
    for y in range(-K,K+1):
        z=x-y
        z=b-z
        z=max(0,z)
        m=min(m,z)
print(m)


