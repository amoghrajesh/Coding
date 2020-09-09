class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = version1.split('.')
        b = version2.split('.')
        
        m = len(a)
        n = len(b)
        
        if m > n:
            d = m - n
            b += ['0'] * d
        if n > m:
            d = n - m
            a += ['0'] * d
        
        a = list(map(int, a))
        b = list(map(int, b))
        
        if a == b:
            return 0
        
        n = len(a)
        i = 0
        while i < n:
            if a[i] == b[i]:
                i += 1
            elif a[i] > b[i]:
                return 1
            else:
                return -1