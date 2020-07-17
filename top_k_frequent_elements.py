from collections import Counter
from heapq import heapify, nlargest
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        l = list(c.items())
        heapify(l)
        n = nlargest(k, l, key = lambda z: z[1])
        return [i[0] for i in n]