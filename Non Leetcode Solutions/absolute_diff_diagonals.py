matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]
n = 4
diff = 0
s1 =0
s2=0
for i in range(n):
    s1 += matrix[i][i]
    s2 += matrix[i][n-1-i]
print(s1-s2)