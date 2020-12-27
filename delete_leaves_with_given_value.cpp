class Solution {
public:
    TreeNode* postorder(TreeNode* root, int target){
        if(!root){
            return NULL;
        }
        
        root->left = postorder(root->left, target);
        root->right = postorder(root->right, target);
        
        if(!root->left && !root->right && !(root->val - target)){
            return NULL;
        }
        return root;
    }
    
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        // need a traversal that will check leaves firts and then root
        return postorder(root, target); 
    }
};