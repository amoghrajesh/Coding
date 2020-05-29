def minCoins(amount,coins):
	m=len(coins)
	dp=[]
	big=10**10
	for i in range(amount+1):
		dp.append(big)
	dp[0]=0
	
	for i in range(1,amount+1):
		#all coins
		for j in range(m):
			if coins[j]<=i:
				prev=dp[i-coins[j]]
				if prev!=big and prev+1<dp[i]:
					dp[i]=prev+1
	return dp[-1]
		
	
	

n=int(input())
#find all perfect squares less than this number
p=1
coins=[]
while p*p<=n:
	coins.append(p*p)
	p+=1
print(coins)


return minCoins(n,coins)