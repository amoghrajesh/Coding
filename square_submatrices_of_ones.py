matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

m = len(matrix)
n = len(matrix[0])

for i in range(1,m):
    for j in range(1,n):
        if matrix[i][j] == 0:
            continue
        else:
            matrix[i][j] =  min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1]) + 1
ans = 0
for i in matrix:
    ans += sum(i)

print(ans)






