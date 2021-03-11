class Solution {
    public int coinChange(int[] coins, int amount) {
        int n = coins.length;
        if(n == 0){
            return -1;
        }
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        int lookback;
        
        for(int i = 1; i < amount + 1; i++){
            for(int j = 0; j < n; j++){
                if(coins[j] <= i){
                    lookback = dp[i - coins[j]];
                    if(lookback != Integer.MAX_VALUE){
                        dp[i] = Math.min(1 + lookback, dp[i]);
                    }
                }
            }
        }
        return dp[amount] != Integer.MAX_VALUE ? dp[amount] : -1;
    }
}
