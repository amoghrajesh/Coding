import numpy as np
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)
        m = 3 * n - 2
        
        A = np.array(A)
        B = np.array(B)
        
        padded = [[0] * m] * m
        padded = np.array(padded)
        padded[n - 1: n - 1 + n, n - 1: n - 1 + n] = B
        ans = -10 ** 9  
        for i in range(2 * n - 1):
            for j in range(2 * n - 1):
                subarray = padded[i: i + n, j : j + n]
                temp = 0
                temp = np.sum(A * subarray)
                # for k in range(n):
                #     for l in range(n):
                #         temp += (A[k][l] * subarray[k][l])
                ans = max(ans, temp)
        return ans