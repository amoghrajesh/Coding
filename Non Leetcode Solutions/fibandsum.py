from math import gcd
from math import sqrt

def fib(n):
    f=((1+sqrt(5))/2)**n - ((1-sqrt(5))/2)**n
    f=f/sqrt(5)
    return int(f)

n,k=input().split()
n,k=int(n),int(k)
a=list(map(int,input().split()))
res=0
for i in range(n-1):
    for j in range(i+1,n):
        ai=a[i]
        aj=a[j]
        ai=int(ai**k)
        aj=int(aj**k)
        g=gcd(ai,aj)
        res+=fib(g)
print(res)

