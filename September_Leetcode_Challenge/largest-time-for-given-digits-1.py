from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        perm = list(permutations(A))
        ans = -10**9
        for i in range(len(perm)):
            a, b, c, d = perm[i]
            h = 10 * a + b
            m = 10 * c + d
            if h < 24 and m < 60:
                ans = max(ans, h * 60 + m)
        
        if ans == -10**9:
            return ""
        else:
            h = ans // 60
            m = ans % 60
            return "{:02d}:{:02d}".format(h, m)