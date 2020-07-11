#include <cstdlib>
class Solution {
public:
    vector<int> data;
    TreeNode* newNode(int val){
        TreeNode* node = (TreeNode*)malloc(sizeof(TreeNode));
        node->val = val;
        node->left = node->right = NULL;
        return node;
    }
    void inorder(TreeNode* root){
        if(!root){
            return;
        }
        inorder(root->left);
        data.push_back(root->val);
        inorder(root->right);
    }
    
    TreeNode* increasingBST(TreeNode* root) {
        if(!root){
            return root;
        }
        inorder(root);
        TreeNode* h = newNode(data[0]);
        TreeNode* temp = h;
        for(int i = 1; i<data.size(); i++){
            TreeNode* node = newNode(data[i]);
            temp->right = node;
            temp = temp->right;
        }
        return h;
    }
};