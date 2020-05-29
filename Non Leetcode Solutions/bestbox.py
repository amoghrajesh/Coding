from math import sqrt
def getl(p,a):
    l1=(p-sqrt(p**2 - 24*a))/12
    l2=(p-sqrt(p**2 - 24*a))/12
    return l1

def get_vol(l,a,p):
    return l**3 - (l**2 * p/4) + a*l/2

t=int(input())
for i in range(t):
    p,a=list(map(int,input().split()))
    l=getl(p,a)
    #print(l)
    v=get_vol(l,a,p)
    v=round(v,2)
    print(v)
