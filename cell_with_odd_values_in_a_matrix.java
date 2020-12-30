class Solution {
    public int oddCells(int n, int m, int[][] indices) {
        HashMap<Integer, Integer> row = new HashMap<>();
        HashMap<Integer, Integer> col = new HashMap<>();
        int mat[][] = new int[n][m];
        for(int i = 0; i < indices.length; i++){
            if(row.containsKey(indices[i][0]) == false){
                row.put(indices[i][0], 1);
            }
            else{
                row.put(indices[i][0], row.get(indices[i][0]) + 1);
            }
        }
        for(int i = 0; i < indices.length; i++){
            if(col.containsKey(indices[i][1]) == false){
                col.put(indices[i][1], 1);
            }
            else{
                col.put(indices[i][1], col.get(indices[i][1]) + 1);
            }
        }
        
        for(Map.Entry<Integer, Integer> e: row.entrySet()){
            for(int i = 0; i < m; i++){
                mat[e.getKey()][i] += e.getValue();
            }
        }
        for(Map.Entry<Integer, Integer> e: col.entrySet()){
            for(int i = 0; i < n; i++){
                mat[i][e.getKey()] += e.getValue();
            }
        }
        int ans = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(mat[i][j] % 2 == 1){
                    ans++;
                }
            }
        }
        return ans;
    }
}