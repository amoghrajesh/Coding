class Solution {
    int mod = 1000000007;
    
    public int helper(int[][][] dp, int m, int n, int moves, int i, int j){
        if(i < 0 || j < 0 || i >= m || j >= n){
            return 1;
        }
        
        if(moves <= 0){
            return 0;
        }
        if(dp[i][j][moves] != 0){
            return dp[i][j][moves];
        }
        
        int count = 0;
        count += helper(dp, m, n, moves - 1, i - 1, j) % mod;
        count += helper(dp, m, n, moves - 1, i, j + 1) % mod;
        count += helper(dp, m, n, moves - 1, i + 1, j) % mod;
        count += helper(dp, m, n, moves - 1, i, j - 1) % mod;

        dp[i][j][moves] = count % mod;
        return dp[i][j][moves];
    }
    
    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        int[][][] dp = new int[m][n][maxMove + 1];
        
        return helper(dp, m, n, maxMove, startRow, startColumn);
    }
}
