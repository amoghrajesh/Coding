from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        vis = defaultdict(bool)
        mi, ma = min(nums), max(nums)
        
        for i in nums:
            vis[i] = True
        
        c, ans = 0, -1
        for i in range(mi, ma + 1):
            if vis[i] == False:
                ans = max(ans, c)
                c = 0   
            else:
                c += 1
        return max(ans, c)
