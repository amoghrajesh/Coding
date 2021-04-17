class Solution {
    public int numSubmatrixSumTarget(int[][] matrix, int k) {
        int m = matrix[0].length, n = matrix.length;
        for(int i = 1; i<n; i++){
            for(int j = 0; j<m; j++){
                matrix[i][j] += matrix[i-1][j];
            }
        }
        
        int count = 0;
        for(int base = 0; base <n ; base++){
            
            for(int row = base; row<n; row++){
                
                HashMap<Integer,Integer> map = new HashMap<>();
                map.put(0,1);
                int prefixsum = 0;
                
                for(int j = 0; j<m ; j++){
                    
                    prefixsum += matrix[row][j] - (base != 0 ? matrix[base - 1][j] : 0);
                    count += map.getOrDefault(prefixsum - k, 0);
                    map.put(prefixsum, map.getOrDefault(prefixsum,0) + 1);
                    
                }
            }
        }
        return count;
    }
}
