class Solution {
    public int maxProfit(int[] prices, int fee) {
        int n = prices.length;
        int noStocks = 0;
        int oneStocks = -prices[0];
        
        for(int i = 1; i < n; i++){
            noStocks = Math.max(noStocks, oneStocks + prices[i] - fee);
            oneStocks = Math.max(oneStocks, noStocks - prices[i]);
        }
        
        return noStocks;
    }
}
