from math import sqrt
def primefactors(n):
    prime=[]
    while n%2==0:
        prime.append(2)
        n=n//2
    for i in range(3,int(sqrt(n)),2):
        while n%i==0:
            prime.append(i)
            n//=i
    if n>2:
        prime.append(n)
    return prime


n=input()
prime=primefactors(int(n))
s=sum(map(int,n))

x=0
for i in prime:
    j=str(i)
    x+=sum(map(int,j))
if s==x:
    print(1)
else:
    print(0)
