class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        ans = 0
        while z:
            b = z % 2
            if b == 1:
                ans += 1
            z//=2
        return ans