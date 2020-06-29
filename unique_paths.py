from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        right = m - 1
        down = n - 1
        return factorial(right + down)//(factorial(right) * factorial(down))