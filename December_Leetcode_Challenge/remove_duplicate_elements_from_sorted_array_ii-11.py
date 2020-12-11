class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        while i < len(nums):
            temp = nums[: i]
            if temp.count(nums[i]) == 2:
                nums.pop(i)
                continue
            else:
                i += 1
        return len(nums)