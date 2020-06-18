class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n == 0:
            return 0
        l = 0
        r = n
        while l<r:
            m = l + (r - l)//2
            if n - m <=citations[m]:
                r = m
            else:
                l = m + 1
        
        return n - l