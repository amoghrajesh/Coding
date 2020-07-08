class Solution(object):    
    def threeSum(self, nums):
        ans = set()
        val = 0
        n = len(nums)
        nums.sort()
        exp = 0
        for i in range(n-2):
            l = i + 1
            r = n - 1
            while l < r:
                obs = nums[i] + nums[l] + nums[r]
                if exp == obs:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif exp < obs:
                    r -= 1
                else:
                    l += 1
        return [[i[0], i[1], i[2]] for i in ans]