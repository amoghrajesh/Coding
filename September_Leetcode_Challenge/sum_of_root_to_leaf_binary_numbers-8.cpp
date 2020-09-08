class Solution {
public:
    void addSum(int &ans, vector<int> &path){
        int x = 0;
        int n = path.size();
        for(int i = n - 1; i >= 0; i--){
            ans += (1 << x) * path[i];
            x++;
        }
    }
    
    void findAllPaths(int &ans, TreeNode* root, vector<int> &path){
        if(!root){
            return;
        }
        
        path.push_back(root->val);
        
        if(!root->left && !root->right){
            addSum(ans, path);    
        }
        findAllPaths(ans, root->left, path);
        findAllPaths(ans, root->right, path);
        
        path.pop_back();
        
    }
    int sumRootToLeaf(TreeNode* root) {
        vector<int> path;
        int ans = 0;
        
        findAllPaths(ans, root, path);
        return ans;
    }
};