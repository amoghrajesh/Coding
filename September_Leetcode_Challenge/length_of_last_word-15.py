class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split()
        n = len(x)
        f = 0
        for i in range(n-1, -1, -1):
            if len(x[i]) != 0:
                f = 1
                return len(x[i])
        if f == 0:
            return 0