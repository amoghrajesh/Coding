class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sortedA = sorted(A, reverse = True)
        sortedB = sorted(enumerate(B), key = lambda x: (x[1], x[0]), reverse = True)
        n = len(A)
        ans = [-1] * n
        j = 0
        
        for i, (index, value) in enumerate(sortedB):
            if sortedA[i] > value:
                ans[index] = sortedA[i]
                j += 1
        for i in range(n):
            if ans[i] == -1:
                ans[i] = sortedA[j]
                j += 1
        return ans
        
