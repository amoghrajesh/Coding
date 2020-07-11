class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power = []
        for i in range(0, 2**len(nums)):
            b = bin(i)[2:].zfill(len(nums))
            temp = []
            for j in range(len(b)):
                if b[j] == '1':
                    temp.append(nums[j])
            power.append(temp)
        return power