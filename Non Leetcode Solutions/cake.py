t=int(input())
for i in range(t):
    d=dict()
    s=input()
    se=set(s)
    for j in se:
        if j not in d:
            d[j]=list(s).count(j)
    
    m=max(d.values())
    #print(m)
    for k in d:
        if(d[k]==m):
            v=k
        
    
    p=d.pop(v)
    #print(p)
    s=0
    for k in d:
        s+=d[k]
    if(s==p):
        print("YES")
    else:
        print("NO")
    
