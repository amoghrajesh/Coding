class Solution {
public:
    int titleToNumber(string s) {
        int n = s.size();
        int ans = 0;
        int exp = 0;
        for(int i = n - 1; i >= 0; i--){
            ans += (int(pow(26, exp)) * (s[i] - 'A' + 1));
            exp++;
        }
        
        return ans;
    }
};