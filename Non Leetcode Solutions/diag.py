n=int(input())
mat=[]
for i in range(n):
    l=list(map(int,input().split()))
    mat.append(l)

n=len(mat[0])

lead=[mat[i][i] for i in range(n)]
nonlead=[mat[n-1-i][i] for i in range(n-1,-1,-1)]
a=sum(lead)
b=sum(nonlead)
print(abs(a-b))
