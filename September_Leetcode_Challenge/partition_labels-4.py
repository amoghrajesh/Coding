class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_occur = {}
        n = len(S)
        for i in range(n):
            last_occur[S[i]] = i
        
        ans = []
        cur = 0
        while cur < n:
            end = last_occur[S[cur]]
            while cur <= end:
                x = S[cur]
                end = max(last_occur[x], end)
                cur += 1
            if not ans:
                ans.append(cur)
            else:
                ans.append(cur - sum(ans))
        return ans