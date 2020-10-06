class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        TreeNode* temp = new TreeNode();
        temp->val = val;
        temp->left = temp->right = NULL;
        if(!root){
            return temp;
        }
        TreeNode* p = root;
        TreeNode* q;
        
        while(p){
            if(p->val > val){
                q = p;
                p = p->left;        
            }
            else{
                q = p;
                p = p->right;
            }
        }
        if(val < q -> val){
            q->left = temp;
        }
        else{
            q->right = temp;
        }
        return root;
        
    }
};