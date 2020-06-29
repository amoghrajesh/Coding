class Solution(object):
    def uniquePaths(self, m, n):
        def fact(x):
            if x<=2:
                return dp[x]
            else:
                if x<len(dp):
                    return dp[x]
                for i in range(3, x + 1):
                    dp.append(dp[-1] * i)
                return dp[x]
        
        dp = [1, 1, 2]
        
        right = m-1
        down = n-1
        
        f = fact(right + down)
        f1 = fact(right)
        f2 = fact(down)
        
        return f//(f1*f2)