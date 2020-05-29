def sieve(n):
    prime=[True for i in range(n+1)]
    p=2
    while p*p<=n:
        if prime[p]==True:
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    return prime

n=2000000
prime=sieve(n)
ans=[]
for i in range(2,n):
    if prime[i]==True:
        ans.append(i)
print(sum(ans))
