l=list(map(int,input().split()))
n=len(l)
ans=[]
for i in range(n):
    j=(i+1)%n
    a=l[i]
    b=0
    while b!=1 and j!=i:
        if l[j]>a:
            ans.append(l[j])
            b=1
        j=(j+1)%n
    if b==0:
        ans.append(-1)
print(ans)
    