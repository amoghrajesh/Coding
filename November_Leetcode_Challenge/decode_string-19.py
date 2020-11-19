class Solution(object):
    def decodeString(self, s):
        stack = []
        ops = []
        while "[" in s:
            new_s = ""
            for i in range(len(s)):
                if s[i] == "[":
                    stack.append(i)
                if s[i] == "]":
                    j = stack.pop()
                    i, j = j, i
                    t = i
                    while ord(s[t-1]) in range(ord("0"), ord("9")+1):
                        t -= 1
                    new_s = s[:t] + int(s[t:i]) * s[i+1:j] + s[j+1:]
                    s = new_s
                    break
        return s