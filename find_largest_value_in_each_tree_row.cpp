#include<queue>
class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        int size;
        vector<int> ans;
        if(!root){
            return ans;
        }
        queue<TreeNode*> q;
        q.push(root);
        TreeNode* temp;
        int m = INT_MIN;
        
        while(!q.empty()){
            size = q.size();
            m = INT_MIN;
            
            while(size--){
                temp = q.front();
                q.pop();
                m = max(temp->val, m);
                
                if(temp->left){
                    q.push(temp->left);
                }
                if(temp->right){
                    q.push(temp->right);
                }
            }
            ans.push_back(m);
        }
        return ans;
    }
};