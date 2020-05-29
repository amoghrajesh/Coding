ans=[]
for i in range(10,1000000):
    s=str(i)
    l=list(s)
    k=list(map(int,l))
    p=list(map(lambda x:x**5,k))
    if sum(p)==i:
        ans.append(i)
print(sum(ans))
    
