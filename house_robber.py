l=[2,7,9,3,1]
n=len(l)

if n==0:
	print(0)
if n==1:
	print(l[0])

dp=[l[0],max(l[0],l[1])]
for i in range(2,n):
	dp.append(max(l[i]+dp[i-2],dp[i-1]))
print(dp[n-1])