A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
m=len(A)
n=len(B)

i=0
j=0
ans=[]
while i<m and j<n:
    start = max(A[i][0],B[j][0])
    end = min(A[i][1], B[j][1])
    if start<=end:
        ans.append([start, end])

    if A[i][1] < B[j][1]:
        i+=1

    if B[j][1]< A[i][0]:
        j+=1

print(ans)

