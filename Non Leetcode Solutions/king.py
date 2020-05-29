n,q=input().split()
n,q=int(n),int(q)
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(q):
    l,r=input().split()
    l,r=int(l),int(r)
    ans=0
    for j in range(l-1,r):
        ans=ans+(a[j]*b[j])
    print(ans)
