matrix = [[1,2,3],[4,5,6]]
m = len(matrix)
n = len(matrix[0])
ans = []

for i in range(n):
    temp = []
    for j in range(m):
        print(j,i,matrix[j][i])
        temp.append(matrix[j][i])
    ans.append(temp)
print(ans)
