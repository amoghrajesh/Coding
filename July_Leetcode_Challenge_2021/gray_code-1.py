class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = []
        if n == 0:
            return ans
        for i in range(0, 2 ** n):
            b = bin(i)[2:]
            temp = b[0]
            for j in range(1, len(b)):
                temp += str(int(b[j - 1]) ^ int(b[j]))
            ans.append(temp)
        return list(map(lambda x: int(x, 2), ans))
