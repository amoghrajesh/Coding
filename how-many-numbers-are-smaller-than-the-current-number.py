class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x = sorted(nums)
        hashmap = dict()
        for i in range(len(x)):
            if x[i] not in hashmap:
                hashmap[x[i]] = i
        
        ans = []
        for i in nums:
            ans.append(hashmap[i])
        return ans