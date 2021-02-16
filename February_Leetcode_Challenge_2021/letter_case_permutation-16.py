class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        s = S.lower()
        if s.isnumeric():
            return [s]
        ans = []
        alpha = []
        
        for i in range(len(s)):
            if s[i].isalpha():
                alpha.append(i)
        
        n = len(alpha)
        
        for i in range(2 ** n):
            b = bin(i)[2:].zfill(n)
            temp = list(s)
            for j in range(len(b)):
                if b[j] == '1':
                    temp[alpha[j]] = temp[alpha[j]].upper()
            
            ans.append(''.join(temp))
        return ans
