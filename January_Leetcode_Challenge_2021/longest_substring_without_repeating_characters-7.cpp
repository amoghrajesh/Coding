class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        int ans = INT_MIN;
        
        for(int i = 0; i < n; i++){
            vector<bool> visited(256, false);
            for(int j = i; j < n; j++){
                if(visited[s[j]]){
                    break;
                }
                else{
                    visited[s[j]] = true;
                    ans = max(ans, j - i + 1);
                }
            }
            visited[s[i]] = false;
        }
        return ans == INT_MIN ? 0 : ans;
    }
};