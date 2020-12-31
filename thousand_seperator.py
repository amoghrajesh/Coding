class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = ""
        if len(str(n)) <= 3:
            return str(n)
        n = str(n)[::-1]
        for i in range(len(n)):
            ans += n[i]
            if (i + 1) % 3 == 0:
                ans += '.'
        return ans[::-1][1:] if len(str(n)) % 3 == 0 else ans[::-1] 