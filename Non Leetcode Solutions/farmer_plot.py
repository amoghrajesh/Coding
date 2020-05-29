from math import gcd,floor
t=int(input())
for i in range(t):
    l,b=list(map(int,input().split()))
    side=gcd(l,b)
    n=floor((l*b)/(side**2))
    print(n)
    
