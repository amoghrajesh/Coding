class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        substrings = dict()
        n = len(s)
        for i in range(0, n - k + 1):
            substrings[s[i: i + k]] = True
        # print(substrings)
        for i in range(0, 2 ** k):
            b = bin(i)[2:].zfill(k)
            # print(i, b)
            if b not in substrings:
                return False
        return True
