class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask = 0
        ans = 0
        
        for i in range(31, -1, -1):
            mask = mask | 1 << i
            s = set()
            for num in nums:
                s.add(num & mask)
            
            start = ans | 1 << i
            
            for prefix in s:
                if start ^ prefix in s:
                    ans = start
        return ans
        