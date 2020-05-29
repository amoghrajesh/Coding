matrix=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

n=len(matrix)

x=n//2

for i in range(n):
	#to cover all columns
	for j in range(x):
		matrix[j][i],matrix[n-1-j][i]=matrix[n-1-j][i],matrix[j][i]

#Now take the transpose of the matrix


for i in range(n-1):
	for j in range(i+1,n):
		matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
print(matrix)		