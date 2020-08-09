class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int rows = grid.size(), cols = grid[0].size();
        int freshCount = 0, mins = 0;
        queue<pair<int, int>> q;
        vector<vector<int>> dirs = {{0,1}, {0,-1}, {-1, 0}, {1, 0}};
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1)
                    freshCount++;
                else if (grid[i][j] == 2)
                    q.push({i, j});
            }
        }
        
        if (freshCount == 0)
            return 0;
        
        while (!q.empty()) {
            int qSize = q.size();
            mins++;
            
            while (qSize--) {
                auto [i, j] = q.front(); q.pop();
                
                for (auto& dir : dirs) {
                    int x = i + dir[0];
                    int y = j + dir[1];
                    
                    if (x >= 0 and x < rows and y >= 0 and y < cols and grid[x][y] == 1) {
                        grid[x][y] = 2;
                        q.push({x, y});
                        freshCount--;
                    }
                }
            }
            
            if (freshCount == 0)
                break;            
        }
        
        if (freshCount > 0)
            return -1;
        
        return mins;
    }
};