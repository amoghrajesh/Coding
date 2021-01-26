#include<queue>
class Solution {
public:
    bool outBound(int x, int y, int m, int n){
        return x < 0 || y < 0 || x >= m || y >= n;    
    }
    
    int minimumEffortPath(vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();
        
        int dp[m + 1][n + 1];
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                dp[i][j] = INT_MAX;
            }
        }
        dp[0][0] = 0;
        
        queue<pair<int, int>> q;
        q.push({0, 0});
        int x[4] = {0, -1, 0, 1};
        int y[4] = {-1, 0, 1, 0};
        pair<int, int> temp;
        int px, py;
        
        while(!q.empty()){
            temp = q.front();
            q.pop();
            
            for(int k = 0; k < 4; k++){
                px = temp.first + x[k];
                py = temp.second + y[k];
                if(outBound(px, py, m, n)){
                    continue;
                }
                if(dp[px][py] <= dp[temp.first][temp.second]){
                    continue;
                }
                
                dp[px][py] = min(dp[px][py], max(dp[temp.first][temp.second], abs(heights[temp.first][temp.second] - heights[px][py])));
                q.push({px, py});
            }
            
        }
        
        return dp[m - 1][n - 1];
        
    }
};
