class Solution {
public:
    TreeNode* inorder_successor(TreeNode* root){
        TreeNode* p = root;
        while(p && p->left){
            p = p->left;
        }
        return p;
    }
    
    TreeNode* deleteNode(TreeNode* root, int key) {
        if(!root){
            return root;
        }
        
        if(key < root->val){
            root->left = deleteNode(root->left, key);
        }
        else if(key > root->val){
            root->right = deleteNode(root->right, key);
        }
        
        else if(key == root->val){
            if(!root->left){
                TreeNode* temp = root->right;
                delete root->left;
                return temp;
            }
            else if(!root->right){
                TreeNode* temp = root->left;
                delete root->right;
                return temp;
            }
            
            TreeNode* temp = inorder_successor(root->right);
            //get inorder succesor
            root->val = temp->val;
            root->right = deleteNode(root->right, temp->val);
        }
        return root;
    }
};