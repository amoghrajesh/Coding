class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int mincost = INT_MAX;
        
        for(int i = 0; i < prices.size(); i++){
            mincost = min(prices[i], mincost);
            profit = max(profit, prices[i] - mincost);
        }
        return profit;
    }
};