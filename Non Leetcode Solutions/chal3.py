t=int(input())

for i in range(t):
    n=int(input())
    k=str(n)
    more=int(k[::-1])
    ans=int(k)
    for j in range(1,n+1):
        s=str(j)
        rev=s[::-1]
        if(int(rev)>more):
            ans=s
    print(ans)        
        
