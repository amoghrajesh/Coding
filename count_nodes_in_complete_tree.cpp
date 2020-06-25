class Solution {
public:
    
    int lheight(TreeNode* root){
        int h = 0;
        while(root){
            h++;
            root = root->left;
        }
        return h;
    }
    
    int rheight(TreeNode* root){
        int h = 0;
        while(root){
            h++;
            root = root->right;
        }
        return h;
    }
    
    int countNodes(TreeNode* root) {
        
        if(root == NULL){
            return 0;
        }
        
        int l = lheight(root);
        int r = rheight(root);
        
        if(l == r){
            return (1<<l)-1;
        }
        
        return 1 + countNodes(root->left) + countNodes(root->right);
        
    }
};