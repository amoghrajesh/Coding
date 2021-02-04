from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 0
        
        for k in freq:
            if k + 1 in freq:
                ans = max(ans, freq[k] + freq[k + 1])
        return ans
