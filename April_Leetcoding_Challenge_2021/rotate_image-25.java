class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        if(n == 1){
            return;
        }
        int[][] transpose = new int[n][n];
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                transpose[i][j] = matrix[j][i];
            }
        }
            
        int half = n / 2;
        int temp;
        
        for(int h = 0; h < half; h++){
            for(int row = 0; row < n; row++){
                temp = transpose[row][h];
                transpose[row][h] = transpose[row][n - 1 - h];
                transpose[row][n - 1 - h] = temp;
            } 
        }
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                matrix[i][j] = transpose[i][j];
            }
        }

    }
}
