class Solution:
    def toGoatLatin(self, s: str) -> str:
        vow = ['a', 'e', 'i', 'o', 'u']
        l = s.split()
        ans = []
        
        for i in range(len(l)):
            w = l[i]
            if w[0].lower() not in vow:
                w = w[1: len(s)] + w[0] 
            w =  w + "ma"
            base = "a" * ( i + 1)
            w = w + base
            ans.append(w)
        return ' '.join(ans)