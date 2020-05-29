t=int(input())
for i in range(t):
    n,m,k=input().split()
    n,m,k=int(n),int(m),int(k)
    d=abs(n-m)-k
    if(d<0):
        print(0)
    else:
        print(d)
