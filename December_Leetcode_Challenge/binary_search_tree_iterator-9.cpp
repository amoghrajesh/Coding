class BSTIterator {
public:
    vector<int> v;
    int p;
    int n;
    
    void inorder(TreeNode* root){
            
        if(!root){
            return;
        }
        
        inorder(root->left);
        v.push_back(root->val);
        inorder(root->right);
    }
    
    BSTIterator(TreeNode* root) {
        inorder(root);
        n = v.size();
        p = 0;
    }
    
    int next() {
        int a = v[p];
        p++;
        return a;
    }
    
    bool hasNext() {
        return p < n;   
    }
};