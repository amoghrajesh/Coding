t=int(input())
for i in range(t):
    n,k,v=input().split()
    n,k,v=int(n),int(k),int(v)
    l=list(map(int,input().split()))
    s=sum(l)
    ans=(((n+k)*v)-s)
    
    if(ans>0 and ans%k==0):
        print(ans//k)
    else:
        print(-1)
