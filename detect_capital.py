class Solution:
    def detectCapitalUse(self, s: str) -> bool:
        if not s or s.isupper() or s.islower():
            return True
        
        if s[0].isupper() and s[1:].islower():
            return True
        
        return False