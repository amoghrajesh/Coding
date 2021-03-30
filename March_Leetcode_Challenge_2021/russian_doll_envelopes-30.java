class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        int n = envelopes.length;
        if(n == 0){
            return 0;
        }
        Arrays.sort(envelopes, (a, b) -> {
            if(a[0] != b[0]){
                return a[0] - b[0];
            }
            return a[1] - b[1];
        });
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < i; j++){
                if(envelopes[j][0] < envelopes[i][0] && envelopes[j][1] < envelopes[i][1]){
                    if(dp[i] < dp[j] + 1){
                        dp[i] = dp[j] + 1;
                    }
                }
            }
        }
        
        int m = Integer.MIN_VALUE;
        for(int i: dp){
            m = Math.max(m, i);
        }
        return m;

    }
}
