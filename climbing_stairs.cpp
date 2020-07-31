class Solution {
public:
    int climbStairs(int n) {
        if(n < 0){
            return 0;
        }
        
        if(n == 0 || n == 1){
            return 1;
        }
        
        vector<int> dp;
        dp.push_back(1); //0
        dp.push_back(1); //1
        
        for(int i = 2; i <= n; i++){
            dp.push_back(dp[i-1] + dp[i-2]);
        }
        return dp[n];
    }
};