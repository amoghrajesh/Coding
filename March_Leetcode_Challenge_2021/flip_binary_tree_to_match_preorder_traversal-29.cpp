/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int pos = 0;
    vector<int> ans;
    bool dfs(TreeNode* root, vector<int>& voyage){
        if(pos == voyage.size() || !root){
            return true;
        }
        if(root->val != voyage[pos]){
            return false;
        }
        
        pos++;
        if(pos < voyage.size() && root->left && root->left->val != voyage[pos]){
            ans.push_back(root->val);
            TreeNode* p = root->left;
            root->left = root->right;
            root->right = p;
        }
        bool l = dfs(root->left, voyage);
        bool r = dfs(root->right, voyage);
        
        return l && r;
    }
    vector<int> flipMatchVoyage(TreeNode* root, vector<int>& voyage) {
        if(!root){
            return ans;
        }
        pos = 0;
        bool b = dfs(root, voyage);
        if(!b){
            ans.clear();
            ans.push_back(-1);
        }
        return ans;
    }
};
