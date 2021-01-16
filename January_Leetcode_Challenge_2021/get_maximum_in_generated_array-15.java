class Solution {
    public int getMaximumGenerated(int n) {
        if(n == 0){
            return 0;
        }
        if(n == 1){
            return 1;
        }
        int dp[] = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        int j;
        
        for(int i = 2; i <= n; i++){
            if(i % 2 == 0){
                j = i / 2;
                dp[i] = dp[j];
            }
            else{
                j = i / 2;
                dp[i] = dp[j] + dp[j + 1];
            }
        }
        int m = Integer.MIN_VALUE;
        for(int i: dp){
            if(i > m){
                m = i;
            }
        }
        return m;
    }
}
