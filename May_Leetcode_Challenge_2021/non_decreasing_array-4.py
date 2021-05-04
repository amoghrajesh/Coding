class Solution:
    def checkPossibility(self, A):
        i = 0
        while i < len(A) - 1 and A[i] <= A[i + 1]:
            i += 1
        
        j = len(A) - 1
        while j > 0 and A[j - 1] <= A[j]:
            j -= 1
        
        return (j <= i) or \
                (j - i == 1 and j == len(A) - 1) or \
                (j - i == 1 and i == 0) or \
                (j - i == 1 and A[i - 1] <= A[j]) or \
                (j - i == 1 and A[i] <= A[j + 1])
