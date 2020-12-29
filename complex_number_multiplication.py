class Solution:
    def complexNumberMultiply(self, c1: str, c2: str) -> str:
        a, b = c1.split("+")
        c, d = c2.split("+")
        
        a, c = int(a), int(c)
        b, d = int(b[0: len(b) - 1]), int(d[0: len(d) - 1])
        
        real = a * c - b * d
        imag = a * d + b * c
        ans = str(real) + "+" + str(imag) + "i"
        return ans