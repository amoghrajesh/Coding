class Solution {
public:
    void pathFind(TreeNode* root, vector<int> &v, vector<int> &dist){
        if(!root){
            return;
        }
        v.push_back(root -> val);
        
        if(!root->left && !root->right){
            dist.push_back(v.size());
        }
        
        pathFind(root->left, v, dist);
        pathFind(root->right, v, dist);
        
        v.pop_back();
        
    }
    int minDepth(TreeNode* root) {
        if(!root){
            return 0;
        }
        vector<int> v;
        vector<int> dist;
        pathFind(root, v, dist);
        
        return *min_element(dist.begin(), dist.end());
    }
};