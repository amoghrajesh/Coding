class Solution {
    public int diagonalSum(int[][] mat) {
        int n = mat.length;
        int ans = 0;
        
        for(int i = 0; i < n; i++){
            ans += mat[i][i];    
        }
        
        int r = n - 1;
        int c = 0;
        
        while(r > -1){
            ans += mat[r--][c++];
        }
        if(n % 2 == 1){
            ans -= mat[n/2][n/2];
        }
        return ans;
    }
}