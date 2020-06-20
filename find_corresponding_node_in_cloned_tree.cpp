/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    
    TreeNode* inorder(TreeNode* root, int target){
        if(root==NULL){
            return NULL;
        }
        if(root->val == target){
            return root;
        }
        TreeNode* temp = inorder(root->left, target);
        if(temp != NULL){
            return temp;
        }
        return inorder(root->right, target);
    }
    
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        
        if(target == NULL){
            return NULL;
        }
        return inorder(cloned, target->val);
        
    }
};