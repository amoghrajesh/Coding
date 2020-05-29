t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    r=list(map(int,input().split()))
    mul=[]
    for j in range(len(l)):
        mul.append(l[i]*r[i])
    maxmul=max(mul)
    occ=[]
    for i in range(len(r)):
        if maxmul==mul[i]:
            occ.append(i)
    rs=[]
    for i in occ:
        rs.append(r[i])
    ind=r.index(max(rs))
    print(ind+1)
    
