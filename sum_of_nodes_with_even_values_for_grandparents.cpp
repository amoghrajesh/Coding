class Solution {
public:
    int ans = 0;
    void preorder(TreeNode* root, TreeNode* grandparent, TreeNode* parent){
        if(!root){
            return;
        }
        
        if(grandparent && !(grandparent->val % 2)){
            ans += root->val;
        }
        
        grandparent = parent;
        parent = root;
        
        preorder(root->left, grandparent, parent);
        preorder(root->right, grandparent, parent);
    }
    
    int sumEvenGrandparent(TreeNode* root) {
        if(!root){
            return 0;
        }
        if(!root->left && !root->right){
            return 0;
        }
        preorder(root, NULL, NULL);
        return ans;
    }
};