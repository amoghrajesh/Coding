from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = set()
        freq = Counter(s)
        
        for i in range(len(s)):
            freq[s[i]] -= 1
            if s[i] not in visited:
                while stack and s[i] < stack[-1] and freq[stack[-1]]:
                    visited.remove(stack[-1])
                    stack.pop()
                visited.add(s[i])
                stack.append(s[i])
        return ''.join(stack)