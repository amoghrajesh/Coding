class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashmap = dict()
        for i in range(len(s) - 10 + 1):
            if s[i: i + 10] in hashmap:
                hashmap[s[i: i + 10]] += 1
            else:
                hashmap[s[i: i + 10]] = 1
        
        ans = set()
        
        for i in hashmap:
            if hashmap[i] > 1:
                ans.add(i)
        return list(ans)