class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        ans = []
        for word in queries:
            if word in wordlist:
                ans.append(word)
            else:
                l = word.lower()
                cap = False
                for i in wordlist:
                    j = i.lower()
                    if not cap and j == l:
                        cap = True
                        ans.append(i)
                if not cap:
                    flag = False
                    for i in wordlist:
                        if len(i) == len(word):
                            i1 = ""
                            for x in i.lower():
                                if x not in ['a', 'e', 'i', 'o', 'u']:
                                    i1 += x
                            word1 = ""
                            for x in word.lower():
                                if x not in ['a', 'e', 'i', 'o', 'u']:
                                    word1 += x
                            if not flag and i1 == word1:
                                flag = True
                                ans.append(i)
                    if not cap and not flag:
                        ans.append("")
        print(ans)
        return ans
                    
                            
                            
        
