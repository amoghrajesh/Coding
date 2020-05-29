n,k=list(map(int,input().split()))
x=list(map(int,input().split()))
i=0
trans=0
while i<n:
    trans+=1
    loc=x[i]+k
    while i<n and x[i]<=loc:
        i+=1
    i-=1
    loc=x[i]+k
    while i<n and x[i]<=loc:
        i+=1
print(trans)
    
