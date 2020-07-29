#include <vector>
#include <algorithm>
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() <= 1){
            return 0;
        }
        
        if(prices.size() == 2){
            if(prices[0] > prices[1]){
                return 0;
            }
            else{
                return prices[1] - prices[0];
            }
        }
        int n = prices.size();
        vector<vector<int>>dp(n, vector<int>(2, 0));
        
        dp[0][0] = -1 * prices[0];
        dp[0][1] = 0;
        dp[1][0] = -1 * min(prices[1], prices[0]);
        dp[1][1] = max(0, prices[1] - prices[0]);
        
        for(int i = 2; i < n; i++){
            dp[i][0] = max(dp[i-1][0], dp[i-2][1] - prices[i]);
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i]);
        }
        return dp[n - 1][1];
    }
};