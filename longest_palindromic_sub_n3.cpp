class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        if(n == 0){
            return "";
        }
        int maxlen = 1;
        int flag = 0;
        int start = 0;
        for(int i = 0; i < n; i++){
            for(int j = i; j < n; j++){
                flag = 1;
                string temp = s.substr(i, j - i + 1);
                int sub_len = j - i + 1;
                for(int k = 0; k < sub_len/2; k++){
                    if(temp[k] != temp[sub_len - k - 1]){
                        flag = 0;
                    }
                }
                if(flag && sub_len > maxlen){
                    maxlen = sub_len;
                    start = i;
                }
            }
        }
        cout << s.substr(start, maxlen);
        return s.substr(start, maxlen);
    }
};