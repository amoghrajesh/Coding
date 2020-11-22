class Solution(object):
    def uniqueMorseRepresentations(self, words):
        s = set()
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        for word in words:
            temp = ''
            for i in word:
                index = ord(i) - ord('a')
                temp += morse[index]
            s.add(temp)
        return len(s)