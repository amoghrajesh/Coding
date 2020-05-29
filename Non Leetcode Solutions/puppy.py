t=int(input())
for i in range(t):
    d,n=input().split()
    d,n=int(d),int(n)
    l=list(range(1,n+1))
    for i in range(d):
        s=sum(l)
        l=range(1,s+1)
    print(s)
        
