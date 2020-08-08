class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        if(m == 0 || n == 0){
            return 0;
        }
        
        vector<vector<int>> dp;
        vector<int> v(n, 0);
        
        for(int i = 0; i < m; i++){
            dp.push_back(v);
        }
        
        dp[0][0] = grid[0][0];
        for(int i = 1; i < m; i++){
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }
        for(int i = 1; i < n; i++){
            dp[0][i] = dp[0][i-1] + grid[0][i];
        }
        int cost;
        for(int i = 1; i < m; i++){
            for(int j = 1; j < n ; j++){
                cost = grid[i][j];
                dp[i][j] = min(dp[i][j-1] + cost, dp[i-1][j] + cost);
            }
        }
        return dp[m-1][n-1];
    }
};