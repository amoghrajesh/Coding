from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        if c1 == c2:
            return True
        
        key1 = set(list(c1.keys()))
        key2 = set(list(c2.keys()))
        
        val1 = list(c1.values())
        val2 = list(c2.values())
        
        if key1 == key2 and sorted(val1) == sorted(val2):
            return True
        return False
