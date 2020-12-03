class Solution {
public:
    TreeNode* prev = NULL;
    TreeNode* h = NULL;
    
    void inorder(TreeNode* root){
        if(!root){
            return;
        }
        
        inorder(root->left);
        
        int d = root->val;
        TreeNode* temp = new TreeNode();
        temp->left = temp->right = NULL;
        temp->val = d;
        
        if(prev == NULL){
            prev = temp;
            h = prev;
        }
        
        else{
            
            prev->right = temp;
            prev = temp;
        }
        
        inorder(root->right);
    }
    
    TreeNode* increasingBST(TreeNode* root) {
        inorder(root);
        return h;
    }
};