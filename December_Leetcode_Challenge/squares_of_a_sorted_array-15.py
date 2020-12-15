class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        
        left = 0
        right = n - 1
        x = n - 1
        
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                result[x] = (nums[left] * nums[left])
                left += 1
            else:
                result[x] = (nums[right] * nums[right])
                right -= 1
            x -= 1
        return result