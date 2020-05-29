def change(amount,coins):
	table=[[0]*(amount+1) for i in range(len(coins)+1)]
	
	for i in range(len(table)):
		table[i][0]=1
	
	
	n=len(coins)+1
	m=amount+1
	
	for row in range(1,n):
		for col in range(1,m):
			if col-coins[row-1]>=0:
				table[row][col]=table[row][col-coins[row-1]]+table[row-1][col]
			else:
				table[row][col]=table[row-1][col]
				
	return table[-1][-1]



print(change(5,[1,2,5]))
	