def longestDup(s):

    def rabin_karp(m):
        h = 0
        d = 26
        for i in range(m):
            h = (h * d + asc[i]) % q
        
        a = pow(d, m, q)
        lookup = {h}

        for i in range(1, n - m + 1):
            h = (h * d - asc[i - 1] * a + asc[i + m - 1]) % q
            if h in lookup:
                return i
            lookup.add(h)
        return -1
    q = 2**63 - 1
    n = len(s)
    l = 0
    r = n
    pos = -1
    asc = [ord(x) - ord('a') for x in s]

    while l < r:
        m = l + (r - l)//2
        isFound = rabin_karp(m)
        if isFound!=-1:
            l = m + 1
            pos = isFound
        
        else:
            r = m - 1
    print(s[pos:pos + l - 1])

longestDup("banana")
