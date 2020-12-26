class Solution {
public:
    int numDecodings(string s) {
        int n = s.size();
        if(n == 0){
            return 0;
        }
        
        vector<int> dp(s.size(), 0);
        dp[0] = 1;
        
        if(s[0] != '0'){
            for(int i = 1; i < n; i++){
                if(s[i] != '0'){
                    dp[i] += dp[i - 1];
                }
                if(s[i - 1] == '1' || (s[i - 1] == '2' && (s[i] == '0' || s[i] == '1' || s[i] == '2' || s[i] == '3' || s[i] == '4' || s[i] == '5' || s[i] == '6') )){
                    if(i - 2 > -1){
                        dp[i] += dp[i - 2];
                    }
                    else{
                        dp[i] += 1;
                    }
                }
            }
        }
        else{
            return 0;
        }
        return dp[n - 1];
        
    }
};