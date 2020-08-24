class Solution {
public:
    void helper(TreeNode* root, int &s){
        if(!root){
            return;
        }
        
        if(root->left){
            if(!root->left->left && !root->left->right){
                s += root->left->val;
            }
            helper(root->left, s);
        }
        helper(root->right, s);
        
    }
    
    int sumOfLeftLeaves(TreeNode* root) {
        int s = 0;
        helper(root, s);
        return s;
    }
};