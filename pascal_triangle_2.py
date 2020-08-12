class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = [[1], [1, 1]]
        if rowIndex < 2:
            return l[rowIndex]
        
        for i in range(2, rowIndex + 1):
            prev = l[-1]
            n = len(prev)
            cur = []
            
            for j in range(n - 1):
                cur.append(prev[j] + prev[j+1])
            l.append([1] + cur + [1])
        return l[-1]