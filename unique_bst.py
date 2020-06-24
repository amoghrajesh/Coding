class Solution:
    def numTrees(self, n: int) -> int:
        dp =[1, 1]
        if n<=1:
            return 1
        temp = 0
        for i in range(2, n + 1):
            temp = 0
            for j in range(0, i):
                temp+=(dp[j]*dp[i-j-1])
            dp.append(temp)
        return dp[-1]