t=int(input())
for i in range(t):
    k=int(input())
    p=10**k
    c=0
    for j in range((10**k)//2):
        b=10**k-j-1
        s=set(str(j))
        s1=set(str(b))
        s2=s.union(s1)
        if(len(s2)==2):
            c+=1
    print(2*c)
        
        
