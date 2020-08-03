import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=''
        alpha=string.ascii_lowercase
        nums=string.digits
        s=s.lower()
        for i in s:
            if i in alpha or i in nums:
                new+=i
        
        if new==new[-1::-1]:
            return True
        else:
            return False