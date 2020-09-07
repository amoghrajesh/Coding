class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        hashmap = dict()
        n = len(pattern)
        l = str.split()
        m = len(l)
        
        if m != n:
            return False
        
        for i in range(n):
            if pattern[i] not in hashmap:
                if l[i] in hashmap.values():
                    return False
                else:
                    hashmap[pattern[i]] = l[i]
            else:
                if hashmap[pattern[i]] != l[i]:
                    return False
        return True