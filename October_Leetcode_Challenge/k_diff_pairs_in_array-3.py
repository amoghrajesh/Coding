class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        if k == 0:
            c = Counter(nums).values()
            for i in c:
                if i > 1:
                    ans += 1
            return ans
        
        hashmap = dict()
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        pairs = set()
        for p in nums:
            if p - k in hashmap:
                pairs.add((p, p - k))
        return len(pairs)