class Solution {
public:
    int dfs(vector<vector<int>>& grid, int x, int y, int emp, int steps){
        if(x <= 0 || y <= 0 || x >= grid.size() || y >= grid[0].size() || grid[x][y] == -1){
            return 0;
        }
        if(grid[x][y] == 2){
            if(steps == emp){
                return 1;
            }
            return 0;
        }
        
        grid[x][y] = -1;
        
        int ways = dfs(grid, x, y - 1, emp, steps + 1) + dfs(grid, x - 1, y, emp, steps + 1) + dfs(grid, x, y + 1, emp, steps + 1) + dfs(grid, x + 1, y, emp, steps + 1);
        
        grid[x][y] = 0;
        
        return ways;
        
    }
    
    int uniquePathsIII(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int x, y;
        int emp = 0;
        int steps = 1;
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == 1){
                    x = i;
                    y = j;
                }
                else if(grid[i][j] == 0){
                    emp++;
                }
            }
        }
        return dfs(grid, x, y, emp, steps);
        
    }
};