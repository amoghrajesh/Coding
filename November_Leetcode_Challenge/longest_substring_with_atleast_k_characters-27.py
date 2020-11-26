class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        if k > len(s):
            return 0
        
        f = self.longestSubstring
        char_occ_dict = collections.Counter(s)

        for character, occurrence in char_occ_dict.items():
            
            if occurrence < k:    
                return max( f(sub_string, k) for sub_string in s.split(character) ) 
        return len(s)