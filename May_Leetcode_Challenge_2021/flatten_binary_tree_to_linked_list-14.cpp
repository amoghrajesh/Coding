// Recursive -

class Solution {
public:
    void flatten(TreeNode* root) {
        if(!root){
            return;
        }
        
        flatten(root->left);
        flatten(root->right);
        
        TreeNode* rSubTree = root->right;
        root->right = root->left;
        root->left = NULL;
        
        TreeNode* p = root;
        while(p->right){
            p = p->right;
        }
        
        p->right = rSubTree;
        return;
    }
};

// Iterative -

#include<stack>
class Solution {
public:
    void flatten(TreeNode* root) {
        if(!root){
            return;
        }
        stack<TreeNode*> s;
        s.push(root);
        TreeNode* tail = NULL;
        
        while(!s.empty()){
            TreeNode* temp = s.top();
            s.pop();
            if(!tail){
                tail = temp;
            }
            else{
                tail->right = temp;
                tail->left = NULL;
                tail = temp;
            }
            
            if(temp->right){
                s.push(temp->right);
            }
            if(temp->left){
                s.push(temp->left);
            }
        }
        return;
    }
};
