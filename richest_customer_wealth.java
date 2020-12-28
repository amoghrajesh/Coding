class Solution {
    public int maximumWealth(int[][] accounts) {
        int m = accounts.length;
        if(m == 0){
            return 0;
        }
        int n = accounts[0].length;
        int max = Integer.MIN_VALUE;
        int s;
        
        for(int i = 0; i < m; i++){
            s = 0;
            for(int j = 0; j < n; j++){
                s = s + accounts[i][j];
            }
            if(s > max){
                max = s;
            }
        }
        return max;
    }
}