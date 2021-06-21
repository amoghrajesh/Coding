class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = []
        for i in range(n):
            row = [0 * (i + 1)]
            row[0] = 1
            row[-1] = 1
            for j in range(1, len(row) - 1):
                row[j] = ans[i - 1][j - 1] + ans[i - 1][j]
            ans.append(row)
        return ans    
