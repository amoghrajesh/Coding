class Solution(object):
    def house_robber1(self, nums):
        dp = []
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        dp=[nums[0], max(nums[0],nums[1])]
        
        for i in range(2,n):
            dp.append(max(nums[i] + dp[i-2], dp[i-1]))
        return dp[n-1]
    
        
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        choice1 = nums[:n-1]
        choice2 = nums[1:]
        
        return max(self.house_robber1(choice1), self.house_robber1(choice2))