class Solution {
public:
    int isSafe(vector<vector<int>>& M, int row, int col, vector<bool> visited)
    {
            return (row >= 0) && (row < ROW) && (col >= 0) && (col < COL) && (M[row][col] && !visited[row][col]);
    }
    void dfs(vector<vector<int>>& grid, int row, int col, vector<bool> visited, int& count){
        static int rowNbr[] = { -1, -1, -1, 0, 0, 1, 1, 1 };
        static int colNbr[] = { -1, 0, 1, -1, 1, -1, 0, 1 };
        visited[row][col] = true;

        for (int k = 0; k < 8; ++k)
        {
            if (isSafe(grid, row + rowNbr[k], col + colNbr[k], visited))
            {
                count++;
                dfs(grid, row + rowNbr[k], col + colNbr[k], visited, count);
            }
        }
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int m = grid.size();
        if(!m){
            return 0;
        };
        int n = grid[0].size();
        vector<vector<bool>> visited(m, n, false);
        int ans = 0;
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] && !visited[i][j]){
                    int count = 1;
                    dfs(grid, i, j, count);
                    
                    result = max(result, count);
                }
            }
        }
        return result;
    }
};
