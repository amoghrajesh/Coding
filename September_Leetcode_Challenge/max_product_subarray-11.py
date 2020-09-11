class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev_max_product = prev_min_product = cur_max_product = cur_min_product = ans = nums[0]
        
        for i in range(1, len(nums)):
            cur_max_product = max(prev_max_product * nums[i], prev_min_product * nums[i], nums[i])
            cur_min_product = min(prev_max_product * nums[i], prev_min_product * nums[i], nums[i])
            ans = max(ans, cur_max_product)
            
            prev_max_product = cur_max_product
            prev_min_product = cur_min_product
        return ans