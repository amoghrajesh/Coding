class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        firstBuy = -10**9
        firstSell = 0
        secondBuy = -10**9
        secondSell = 0
        
        for i in prices:
            firstBuy = max(firstBuy, -i)
            firstSell = max(firstSell, firstBuy + i)
            secondBuy = max(secondBuy, firstSell - i)
            secondSell = max(secondSell, secondBuy + i)
        return secondSell