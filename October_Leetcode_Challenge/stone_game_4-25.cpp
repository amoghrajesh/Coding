class Solution {
public:
    bool winnerSquareGame(int n) {
        vector<bool> dp(n+1, false);
        dp[1] = true;
        
        if(n <= 1){
            return dp[n];
        }
        
        for(int i = 2; i < n + 1; i++){
            for(int k = 1; k * k <= i; k++){
                int remainder = i - k * k;
                if(dp[remainder] == false){
                    dp[i] = true;
                    break;
                } 
            }
        }
        return dp[n];
        
    }
};