class Solution {
public:
    int ans = 0;
    void inorder(TreeNode* root, int low, int high){
        if(!root){
            return;
        }    
        
        inorder(root->left, low, high);
        
        if(root->val > high){
            return;
        }
        else if((root->val >= low) && (root->val <= high)){
            ans += root->val;
        }
        
        inorder(root->right, low, high);
    }
    
    int rangeSumBST(TreeNode* root, int low, int high) {
        if(!root){
            return ans;
        }
        inorder(root, low, high);
        return ans;
    }
};