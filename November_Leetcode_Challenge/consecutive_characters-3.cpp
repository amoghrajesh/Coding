class Solution {
public:
    int maxPower(string s) {
        char prev = '#';
        int ans = 0;
        int c = 0;
        
        for(int i = 0; i < s.size(); i++){
            if(s[i] == prev){
                c++;
            }
            else{
                c = 1;
                prev = s[i];
            }
            if(ans < c){
                ans = c;
            }
        }
        return ans;
    }
};