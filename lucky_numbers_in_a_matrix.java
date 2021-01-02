class Solution {
    public List<Integer> luckyNumbers (int[][] matrix) {
        int m = matrix.length;
        List<Integer> ans = new ArrayList<Integer>();
        if(m == 0){
            return ans;
        }
        int n = matrix[0].length;
        
        int row[] = new int[m];
        int col[] = new int[n];
        
        for(int i = 0; i < m; i++){
            int x = Integer.MAX_VALUE;
            for(int j = 0; j < n; j++){
                if(matrix[i][j] < x){
                    x = matrix[i][j];
                }
            }
            row[i] = x;
        }
        
        for(int i = 0; i < n; i++){
            int x = Integer.MIN_VALUE;
            for(int j = 0; j < m; j++){
                if(matrix[j][i] > x){
                    x = matrix[j][i];
                }
            }
            col[i] = x;
        }
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(row[i] == col[j]){
                    ans.add(row[i]);
                }
            }
        }
        return ans;
    }
}