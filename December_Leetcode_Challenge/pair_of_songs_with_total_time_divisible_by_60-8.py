class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        hashmap = dict()
        
        for i in time:
            j = i % 60
            if j in hashmap:
                hashmap[j] += 1
            else:
                hashmap[j] = 1
        
        for i in range(1, 30):
            j = 60 - i
            if i in hashmap and j in hashmap:
                ans += hashmap[i] * hashmap[j]
        
        if 0 in hashmap:
            ans += (hashmap[0] * (hashmap[0] - 1) // 2)
        
        if 30 in hashmap:
            ans += (hashmap[30] * (hashmap[30] - 1) // 2)
            
        return ans