class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if A == B:
            if len(set(A)) < len(list(A)):
                return True
            return False
        m = len(A)
        n = len(B)
        
        if m != n:
            return False
        
        c1 = Counter(A)
        c2 = Counter(B)
        
        if c1 != c2:
            return False
        
        mismatch = 0
        for i in range(m):
            if A[i] != B[i]:
                mismatch += 1
        
        return mismatch == 2