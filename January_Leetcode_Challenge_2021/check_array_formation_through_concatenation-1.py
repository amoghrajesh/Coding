class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        hashmap = dict()
        for start in pieces:
            hashmap[start[0]] = start
        
        ans = []
        for i in arr:
            ans += hashmap.get(i, [])
        
        return ans == arr