import math
def prime(n):
    l=[]
    while n%2==0:
        l.append(2)
        n=n/2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            l.append(int(i))
            n=n/i
    if n>2:
        l.append(int(n))
    return l
p=prime(600851475143)

print(p[-1])
