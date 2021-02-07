class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        left = []
        
        last = -10 ** 9
        for i in range(n):
            if s[i] == c:
                left.append(0)
                last = i
            else:
                left.append(i - last)
        
        last = 10 ** 9
        right = []
        
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                right.append(0)
                last = i
            else:
                right.append(last - i)
        
        right = right[::-1]
        ans = []
        for i in range(n):
            ans.append(min(left[i], right[i]))
        return ans
