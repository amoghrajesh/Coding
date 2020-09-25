class Solution(object):
    def largestNumber(self, nums):
        n = len(nums)
        for i in range(n - 1):
            for j in range(n - 1, i, -1):
                if str(nums[j]) + str(nums[i]) > str(nums[i]) + str(nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
        ans = ""
        for i in nums:
            ans += str(i)
        return str(int(ans))