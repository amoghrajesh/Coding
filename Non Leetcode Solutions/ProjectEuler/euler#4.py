from math import gcd
n=20
ans=1
for i in range(1,n+1):
    ans=(ans*i)//gcd(ans,i)
print(ans)
