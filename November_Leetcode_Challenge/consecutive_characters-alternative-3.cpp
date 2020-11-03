class Solution {
public:
    int maxPower(string s) {
        int ans = 0;
        for(int i = 0; i < s.size(); i++){
            int j = i + 1;
            int c = 1;
            while(j < s.size() && s[j] == s[i]){
                c++;
                j++;
            }
            if(c > ans){
                ans = c;
            }
        }
        return ans;
    }
};