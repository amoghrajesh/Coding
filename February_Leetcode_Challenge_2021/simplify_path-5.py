class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        if path[-1] == '/':
            parts = parts[1:len(parts) - 1]
        else:
            parts = parts[1:len(parts)]
        
        stack = []
        for p in parts:
            if p == '.' or p == '':
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        print(stack)
        ans = '/'
        if not stack:
            return ans
        for i in stack:
            ans += (i + '/')
        return ans[:len(ans) - 1]
