class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int n = s.size();
        for(int i = n / 2; i > 0; i--){
            if(n % i == 0){
                int reps = n / i;
                string r = s.substr(0, i);
                string x = r;
                for(int j = 0; j < reps - 1; j++){
                    x += r;
                }
                if(x == s){
                    return true;
                }
            }
        }
    return false;
    }
};