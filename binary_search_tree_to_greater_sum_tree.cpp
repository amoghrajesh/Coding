class Solution {
public:
    vector<int> v;
    int p = 0;
    
    void inorder(TreeNode* root){
        if(!root){
            return;
        }
        inorder(root->left);
        v.push_back(root->val);
        inorder(root->right);
    }
    
    void manipulate_inorder(TreeNode* root){
        if(!root){
            return;
        }
        
        manipulate_inorder(root->left);
        
        int x = 0;
        for(int i = p; i < v.size(); i++){
            x += v[i];
        }
        root->val = x;
        p++;
        
        manipulate_inorder(root->right);
    }
    
    TreeNode* bstToGst(TreeNode* root) {
        inorder(root);
        manipulate_inorder(root);
        return root;
    }
};