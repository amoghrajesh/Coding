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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> ans;
        if(!root){
            return ans;
        }
        queue<TreeNode*> q;
        q.push(root);
        int size;
        TreeNode* temp;
        long int levelSum = 0;
        int levelN = 0;
        
        while(!q.empty()){
            size = q.size();
            levelN = size;
            levelSum = 0;
            
            while(size--){
                temp = q.front();
                q.pop();
                if(temp->val != 0)
                    levelSum += (temp->val);
                
                if(temp->left){
                    q.push(temp->left);
                }
                if(temp->right){
                    q.push(temp->right);
                }
            }
            ans.push_back(levelSum / (levelN * 1.0));
        }
        return ans;
    }
};
