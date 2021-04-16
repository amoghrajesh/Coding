class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append([char, 1])
            else:
                if stack[-1][0] == char:
                    stack[-1][1] += 1
                else:
                    stack.append([char, 1])

            while stack and stack[-1][1] >= k:
                newtop = stack[-1][1] - k
                if newtop == 0:
                    stack.pop()
                else:
                    stack[-1][1] = newtop
        ans = ""
        for i in stack:
            ans += (i[0] * i[1])
        return ans
