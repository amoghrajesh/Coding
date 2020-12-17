class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        hashmap = dict()
        
        for i in A:
            for j in C:
                if i + j in hashmap:
                    hashmap[i + j] += 1
                else:
                    hashmap[i + j] = 1
        
        ans = 0
        
        for i in B:
            for j in D:
                x = -1 * (i + j)
                ans += hashmap.get(x, 0)
        
        return ans
        