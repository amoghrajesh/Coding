class Solution(object):
    def pancakeSort(self, A):
        S = sorted(A)
        last = len(A) - 1
        ans = []
        while last > 0:
            if A[last] != S[last]:
                m = A.index(S[last])
                A = A[:m+1][::-1] + A[m+1:]
                ans.append(m + 1)
                A = A[:last+1][::-1] + A[last+1:]
                ans.append(last + 1)
            last-=1
        return ans
                