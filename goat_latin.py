class Solution(object):
    def isVowel(self, c):
        c = c.lower()
        return c=='a' or c=='e' or c=='i' or c=='o' or c=='u'
    def toGoatLatin(self, s):
        s = s.split()
        ans = []
        for i in range(len(s)):
            temp = s[i]
            if self.isVowel(s[i][0]):
                pass
            else:
                temp = temp[1:] + temp[0]
            temp+='ma'
            temp+=(i+1)*'a'
            ans.append(temp)
        return ' '.join(ans)