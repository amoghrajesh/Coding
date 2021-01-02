class Solution {
public:
    TreeNode* ans;
    void preorder(TreeNode* root1, TreeNode* root2, TreeNode* target){
        if(!root1){
            return;
        }
        
        preorder(root1->left, root2->left, target);
        preorder(root1->right, root2->right, target);
        if(root1 == target){
            ans = root2;
        }
        
    }
    
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        preorder(original, cloned, target);
        return ans;
    }
};