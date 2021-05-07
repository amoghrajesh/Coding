from collections import Counter
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1 = set(word1)
        w2 = set(word2)
        
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        union = w1.union(w2)
        ans = 0
        
        for i in union:
            if i in c1 and i in c2:
                ans += abs(c1[i] - c2[i])
            else:
                if i in c1:
                    ans += c1[i]
                else:
                    ans += c2[i]
        return ans
