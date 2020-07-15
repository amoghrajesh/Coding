class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        l = s.split(' ')
        l = l[::-1]
        ans = []
        for i in l:
            if i!='':
                ans.append(i)
        return ' '.join(ans)