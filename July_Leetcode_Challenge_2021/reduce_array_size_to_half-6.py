from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        n = len(arr)
        currLen = 0
        
        freq = list(sorted(freq.items(), key = lambda x: x[1]))
        ans = 0
        
        while currLen < n // 2:
            popped = freq.pop()
            currLen += popped[1]
            ans += 1
        return ans
