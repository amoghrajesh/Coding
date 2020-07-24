from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = set(nums)
        f = 0
        for i in nums:
            f ^= i
        
        
        ans = []
        for i in nums:
            x = f ^ i
            if x in s:
                ans.append(i)
        return ansall