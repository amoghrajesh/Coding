class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        if(n == 0){
            return "";
        }
        
        bool dp[n][n];
        memset(dp, 0, sizeof(dp));
        int maxlen = 1;
        int start = 0;
        //dp[i][j] = s[i .. j]
        for(int i = 0; i < n; i++){
            dp[i][i] = true;
        }
        
        for(int i = 0; i < n - 1; i++){
            if(s[i] == s[i+1]){
                dp[i][i+1] = true;
                start = i;
                maxlen = 2;
            }
        }
        
        for(int k = 3; k <= n; k++){
            for(int i = 0; i < (n - k + 1); i++){
                int j = i + (k - 1);
                if((i+1) < n && (j-1) > -1 && s[i] == s[j] && dp[i+1][j-1] == true){
                    dp[i][j] = true;
                    if(k > maxlen){
                        maxlen = k;
                        start = i;
                    }
                }
                
            }
            
        }
        return s.substr(start, maxlen);
    }
};