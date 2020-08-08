    void pathSumHelper(TreeNode* root, int sum, vector<int> &v, int &ans){
        if(!root){
            return;
        }
        
        v.push_back(root->val);
        
        int x = 0;
        for(int i = v.size() - 1; i > -1; i--){
            x += v[i];
            if(x == sum){
                ans++;
            }
        }
        
        pathSumHelper(root->left, sum, v, ans);
        pathSumHelper(root->right, sum, v, ans);
        
        v.pop_back();
        
    }
    
    
    int pathSum(TreeNode* root, int sum) {
        vector<int> v;
        int ans = 0;
        pathSumHelper(root, sum, v, ans);
        return ans;
    }