from itertools import combinations
t=int(input())
for k in range(t):
    n,c=list(map(int,input().split()))
    l=[]
    for j in range(n):
        x=int(input())
        l.append(x)
    l.sort()
    x=list(combinations(l,c))
    m=[]
    for i in x:
        m.append(min(i[2]-i[1],i[1]-i[0]))
    print(max(m))
        
        
