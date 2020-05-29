n=int(input())
"""d={}
for i in range(n):
    x=int(input())
    if x not in d:
        d[x]=0
    d[x]+=1
for i in list(d.items()):
    #print(i)
    if i[1]==1:
        print(i[0])
        break"""
ans=0
for i in range(n):
    x=int(input())
    ans^=x
print(ans)

    
    
