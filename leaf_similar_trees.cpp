class Solution {
public:
    
    void leafs(TreeNode* root, vector<int> &ans){
        if(root == NULL){
            return;
        }
        
        if(root->left == NULL && root->right==NULL){
            ans.push_back(root->val);
        }
        
        leafs(root->left, ans);
        leafs(root->right, ans);
        
        
    }
    
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        
        vector<int> tree1;
        vector<int> tree2;
        leafs(root1, tree1);
        leafs(root2, tree2);
        
        int n1 = tree1.size();
        int n2 = tree2.size();
        if(n1 != n2){
            return false;
        }
        for(int i = 0;i<n1;i++){
            if(tree1[i] != tree2[i]){
                return false;
            }
        }
        return true;

    }
};