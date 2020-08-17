class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        m = len(prices)
        ans = list()
        for i in range(m):
            found = 0
            for j in range(i + 1, m):
                if not found and prices[i] >= prices[j]:
                    ans.append(prices[i] - prices[j])
                    found = 1
            if not found:
                ans.append(prices[i])
        return ans


# O(n) stack based solution
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        m = len(prices)
        ans = prices[:]
        stack = []
        
        for i in range(m):
            while stack and prices[stack[-1]] >= prices[i]:
                ans[stack[-1]] -= prices[i]
                stack.pop()
            stack.append(i)
        return ans