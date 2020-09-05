class Solution {
public:
    void inorder(TreeNode* root, vector<int> &v){
        if(!root){
            return;
        }
        
        inorder(root->left, v);
        v.push_back(root->val);
        inorder(root->right, v);
        
    }
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        vector<int> tree1;
        vector<int> tree2;
        
        inorder(root1, tree1);
        inorder(root2, tree2);
        vector<int> ans;
        
        int i, j;
        i = j = 0;
        int m = tree1.size();
        int n = tree2.size();
        
        while(i < m && j < n){
            if(tree1[i] < tree2[j]){
                ans.push_back(tree1[i]);
                i++;
            }
            else{
                ans.push_back(tree2[j]);
                j++;
            }
        }
        while(i < m){
            ans.push_back(tree1[i]);
            i++;
        }
        while(j < n){
            ans.push_back(tree2[j]);
            j++;
        }
        return ans;
    }
};