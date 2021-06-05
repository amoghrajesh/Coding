class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        sumSpeed = 0
        ans = 0
        heap = []
        
        l = sorted(zip(speed, efficiency), key = lambda x: -x[1])
        for s, e in l:
            if len(heap) > k - 1:
                sumSpeed -= heappop(heap)
            heappush(heap, s)
            sumSpeed += s
            ans = max(ans, sumSpeed * e)
        
        return ans % (10 ** 9 + 7)
