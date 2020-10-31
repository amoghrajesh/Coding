class Solution {
public:
    void inorder_swap(TreeNode* root, TreeNode*& previous, TreeNode*& first, TreeNode*& second){
        if(!root || second != NULL){
            return;
        }
        
        inorder_swap(root->left, previous, first, second);
        
        if(second){
            return;
        }

        if(previous == NULL){
            previous = root;
        }
        else if(first == NULL){
            if(previous->val > root->val){
                first = previous;
            }
        }
        else{
            if(root->val > first->val){
                second = previous;
                int x = first->val;
                first->val = second->val;
                second->val = x;
            }
        }
        
        previous = root;
        
        if(second){
            return;
        }
        
        inorder_swap(root->right, previous, first, second);
    }
    
    void recoverTree(TreeNode* root) {
        TreeNode* first;
        TreeNode* second;
        TreeNode* previous;
        
        
        first = second = previous = NULL;
        
        inorder_swap(root, previous, first, second);
        
        if(second == NULL){
            second = previous;
            int x = first->val;
            first->val = second->val;
            second->val = x;
        }
        return;
    }
};