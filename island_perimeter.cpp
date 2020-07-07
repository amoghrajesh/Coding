class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int ans = 0;
        int n = grid.size();
        int m = grid[0].size();
        int side;
        
        for(int i = 0; i<n; i++){
            for(int j = 0; j<m; j++){
                if(grid[i][j] == 1){
                    side = 0;
                    if(i>0 && grid[i-1][j] == 1){
                        side+=1;
                    }
                    if(j+1<m && grid[i][j+1] == 1){
                        side+=1;
                    }
                    if(i+1<n && grid[i+1][j] == 1){
                        side+=1;
                    }
                    if(j>0 && grid[i][j-1] == 1){
                        side+=1;
                    }
                    
                    ans+=(4 - side);
                }
            }
        }
        return ans;
    }
};