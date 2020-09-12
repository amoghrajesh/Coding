class Solution {
public:
    void helper(vector<vector<int>> &ans, vector<int> &path, int n, int next_start, int k){
        if(n == 0 && path.size() == k){
            ans.push_back(path);
            return;
        }
        
        if(n < 0 || path.size() == k){
            return;
        }
        
        for(int i = next_start; i < 9; i++){
            path.push_back(i + 1);
            helper(ans, path, n - i - 1, i + 1, k);
            path.pop_back();
        }
        
    }
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> ans;
        vector<int> path;
        helper(ans, path, n, 0, k);
        return ans;
    }
};