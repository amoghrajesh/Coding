mat=[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
n=len(mat[0])
m=len(mat)

p=0 #for the row start index
q=0  #for the column start index
ans=[]
while p<m and q<n:
    for i in range(q,n):
        ans.append(mat[p][i])
    p+=1

    for i in range(p,m):
        ans.append(mat[i][n-1])
    n-=1
    
    if p<m:
        for i in range(n-1,q-1,-1):
            ans.append(mat[m-1][i])
        m-=1

    if q<n:
        for i in range(m-1,p-1,-1):
            ans.append(mat[i][q])
        q+=1
return ans









