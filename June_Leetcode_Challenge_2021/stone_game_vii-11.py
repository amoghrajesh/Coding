class Solution:
    def stoneGameVII(self, A: List[int]) -> int:
        N = len(A)
        S = [0] * (N + 1)
        for i in range(1, N + 1):
            S[i] = S[i - 1] + A[i - 1]
        def go(i = 0, j = N - 1):
            if i == j:
                return 0
            L = S[j] - S[i] - go(i, j - 1)
            R = S[j + 1] - S[i + 1] - go(i + 1, j)
            return max(L, R)
        return go()
