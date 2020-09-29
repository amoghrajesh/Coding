from collections import Counter
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        c = Counter(wordDict)
        hashmap = dict()
        def helper(s, size):
            if size == 0:
                return True
            if s in hashmap:
                return hashmap[s]
            for i in range(1, size + 1):
                prefix = s[:i]
                if prefix in c and helper(s[i:], size - i):
                    hashmap[s] = True
                    return True
            hashmap[s] = False
            return False
        
        return helper(s, len(s))