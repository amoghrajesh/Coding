t=int(input())
s=0
for j in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(1,n-1):
        bef=l[:i+1]
        aft=l[i:]
        leftmax=max(bef)
        rightmax=max(aft)
        #print(leftmax,rightmax)
        
        m=min(leftmax,rightmax)
        #print("m",m)
        m-=l[i]
        
        #print("l[i]",l[i])
        #print("x",m)
        s+=m
    print(s)
