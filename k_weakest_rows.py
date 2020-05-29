mat=[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]

n=len(mat[0])
k=int(input())
ans=[]
for i in range(len(mat)):
    j=0
    while j<n and mat[i][j]!=0:
        j+=1
    if j==n:
        ans.append([i,n])
    else:
        ans.append([i,j])
ans.sort(key=lambda x:(x[1],x[0]))
res=[]
for i in range(k):
    res.append(ans[i][0])
    
print(res)
        


