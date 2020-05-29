A = [1,3,7,1,7,5]
B = [1,9,2,5,1]

m = len(A)
n = len(B)
dp=[]
for i in range(m+1):
    dp.append([0]*(n+1))


for i in range(1,m+1):
    for j in range(1,n+1):
        if A[i-1]==B[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
print(dp[-1][-1])