def mypow(a,n):
    if n==0:
        return 1
    else:
        r=mypow(a,n//2)
        if n%2==0:
            return (r*r)%(10**9+7)
        else:
            return (r*a*r)%(10**9+7)
t=int(input())
for i in range(t):
    a,n=list(map(int,input().split()))
    x=mypow(a,n)
    print(x)
             
