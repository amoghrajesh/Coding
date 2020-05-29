t=int(input())
for i in range(t):
    n=int(input())
    l=[]
    for i in range(n):
        s=input()
        l.append(s)
    d=dict()
    for i in l:
        if i not in d:
            d[i]=l.count(i)
    v=list(d.values())
    m=max(v)
    ans=[]
    for i in d:
        if d[i]==m:
            ans.append(i)
    if len(ans)==2:
        print("Draw")
    else:
        print(ans[0])
    
        
        
