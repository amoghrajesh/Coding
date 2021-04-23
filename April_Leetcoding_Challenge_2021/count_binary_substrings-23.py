class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        c = [0, 0]
        c[int(s[0])] += 1
        
        ans = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                c[int(s[i])] += 1
            else:
                c[int(s[i])] = 1
            
            if c[abs(int(s[i]) - 1)] > 0:
                c[abs(int(s[i]) - 1)] -= 1
                ans += 1
        return ans
