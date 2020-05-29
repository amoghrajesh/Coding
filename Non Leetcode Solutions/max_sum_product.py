t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=[]
    for j in range(n-1):
        for k in range(j+1,n):
            p=a[j]*a[k]
            p=str(p)
            #print(p)
            p=sum(map(int,p))
            ans.append(p)
    print(max(ans))
