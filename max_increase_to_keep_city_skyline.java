class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        
        int row[] = new int[m];
        int col[] = new int[n];
        int r = Integer.MIN_VALUE;
        
        for(int i = 0; i < m; i++){
            r = Integer.MIN_VALUE;
            for(int j = 0; j < n; j++){
                if(r < grid[i][j]){
                    r = grid[i][j];
                }
            }
            row[i] = r;
        }
        
        r = Integer.MIN_VALUE;
        for(int i = 0; i < n; i++){
            r = Integer.MIN_VALUE;
            for(int j = 0; j < m; j++){
                if(r < grid[j][i]){
                    r = grid[j][i];
                }
            }
            col[i] = r;
        }
        
        int ans = 0;
        int x, y;
        
        for(int i = 0; i < m; i++){
            x = row[i];
            for(int j = 0; j < n; j++){
                y = col[j];
                if(x == grid[i][j] || y == grid[i][j]){
                    continue;
                }
                else{
                    ans += (Math.min(x, y) - grid[i][j]); 
                }
            }
        }
        return ans;
    }
}