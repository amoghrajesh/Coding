class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = dict()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        trie = self.trie
        for w in word:
            if w not in trie:
                trie[w] = dict()
                trie = trie[w]
            else:
                trie = trie[w]
        trie['exist'] = 1
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._search(word, self.trie)
    
    def _search(self, word:str, cur:dict) -> bool:
        if len(word) == 0:
            return 'exist' in cur
        else:
            if word[0] == '.':
                ans = False
                for key in cur:
                    if key != 'exist':
                        ans = ans or self._search(word[1:], cur[key])
                return ans
            elif word[0] in cur:
                return self._search(word[1:], cur[word[0]])
            else:
                return Falsefind_all