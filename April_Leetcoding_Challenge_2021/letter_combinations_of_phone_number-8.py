class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        ans = []
        if n == 0:
            return ans
        q = []
        hashmap = dict()
        hashmap["2"] = "abc"
        hashmap["3"] = "def"
        hashmap["4"] = "ghi"
        hashmap["5"] = "jkl"
        hashmap["6"] = "mno"
        hashmap["7"] = "pqrs"
        hashmap["8"] = "tuv"
        hashmap["9"] = "wxyz"
        
        for i in hashmap[str(digits[0])]:
            q.append(i)
        
        temp = ""
        for i in range(1, n):
            size = len(q)
            value = digits[i]
            while size:
                temp = q.pop(0)
                for j in hashmap[value]:
                    q.append(str(temp + j))
                size -= 1
        return q
