from math import sqrt, floor
class Solution:
    def arrangeCoins(self, n: int) -> int:
        a = 1
        b = 1
        c = -1 * (2 * n)
        D = b**2 - (4*a*c)
        return floor(-b + floor(sqrt(D)))//(2*a) 
