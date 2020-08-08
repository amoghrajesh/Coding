class Solution {
public:
    void pathSumHelper(TreeNode* root, int sum, vector<int> &v, vector<vector<int>> &ans){
        if(!root){
            return;
        }
        
        v.push_back(root->val);
        
        if(!root->left && !root->right){
            int sum_path = accumulate(v.begin(), v.end(), 0);
            if(sum_path == sum){
                ans.push_back(v);
            }
        }
        
        pathSumHelper(root->left, sum, v, ans);
        pathSumHelper(root->right, sum, v, ans);
        
        v.pop_back();
        
    }
    
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> ans;
        if(!root){
            return ans;
        }
        
        vector<int> v;
        
        pathSumHelper(root, sum, v, ans);
        return ans;
        
    }
};