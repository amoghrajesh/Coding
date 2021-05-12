class NumMatrix {
    private int[][] dp;
    private int[][] mat;
    public NumMatrix(int[][] matrix) {
        if(matrix.length == 0 || matrix[0].length == 0){
            return;
        }
        int m = matrix.length;
        mat = matrix;
        int n = matrix[0].length;
        dp = new int[m][n];
        dp[0][0] = matrix[0][0];
        
        for(int i = 1; i < n; i++){
            dp[0][i] = dp[0][i - 1] + matrix[0][i];
        }
        
        for(int i = 1; i < m; i++){
            dp[i][0] = dp[i - 1][0] + matrix[i][0];
        }
        
        for(int i = 1; i < m; i++){
            for(int j = 1; j < n; j++){
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + matrix[i][j]; 
            }
        }        
        
    }
    
    public int sumRegion(int r1, int c1, int r2, int c2) {

        if(r1 == 0 && r2 == 0 && c1 == 0 && c2 == 0){
            return mat[r1][c1];
        }
        return dp[r2][c2] - dp[r1][c1] + mat[r1][c1] - dp[r2][c1 - 1] + dp[r1][c1 - 1] - dp[r1 - 1][c2] + dp[r1 - 1][c1];
    }
}
