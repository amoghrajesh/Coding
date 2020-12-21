class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        ans = A[-1] - A[0]
        for i in range(1, len(A)): 
            mn = min(A[0] + K, A[i] - K) # move up A[:i]
            mx = max(A[i-1]+K, A[-1] - K) # move down A[i:]
            ans = min(ans, mx - mn)
        return ans 