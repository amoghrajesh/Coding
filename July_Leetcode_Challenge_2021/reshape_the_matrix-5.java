class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        boolean matrixPossible = mat.length * mat[0].length == r * c;
        if(matrixPossible == false){
            return mat;
        }
        int[][] ans = new int[r][c];
        int row, col;
        row = col = 0;
        
        for(int i = 0; i < mat.length; i++){
            for(int j = 0; j < mat[0].length; j++){
                ans[row][col++] = mat[i][j];
                if(col == c){
                    col = 0;
                    row++;
                }
            }
        }
        return ans;
    }
}
