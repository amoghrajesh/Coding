class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        hashmap = dict()
        i = 0
        ans = 0
        for word in words:
            hashmap[i] = set(word)
            i += 1
        
        for i in range(0, n - 1):
            a = hashmap[i]
            for j in range(i + 1, n):
                b = hashmap[j]
                if not len(a.intersection(b)):
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
        
