class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int n = mat.length;
        
        for(int i = 0; i < n; i++){
            int ones = 0;
            for(int j = 0; j < mat[i].length; j++){
                if(mat[i][j] == 1){
                    ones++;
                }
            }
            map.put(i, ones);
        }
        int[][] a = new int[n][2];
        
        int j = 0;
        for(Map.Entry<Integer, Integer> entry: map.entrySet()){
            a[j][0] = entry.getKey();
            a[j][1] = entry.getValue();
            j++;
        }
        
        Arrays.sort(a, (p, q) -> {
                if(p[1] != q[1]){
                    return p[1] - q[1];
                }
                else{
                    return p[0] - q[0];
                }
        });
        
        int[] ans = new int[k];
        for(int i = 0; i < k; i++){
            ans[i] = a[i][0];
        }
        return ans;
    }
}
