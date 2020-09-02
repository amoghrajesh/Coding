class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        if t == 0 and n == len(set(nums)):
            return False
        
        for i in range(n):
            a = nums[i]
            for j in range(i + 1, i + 1 + k):
                if j >= n:
                    break
                if abs(a - nums[j]) <= t:
                    return True
        return False