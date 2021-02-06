#include<queue>
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        if(!root){
            return ans;
        }
        
        queue<TreeNode*> q;
        q.push(root);
        q.push(NULL);
        TreeNode* temp;
        
        while(!q.empty()){
            temp = q.front();
            q.pop();
            if(!temp){
                if(q.empty()){
                    break;
                }
                q.push(NULL);
            }
            else{
                if(q.front() == NULL){
                    ans.push_back(temp->val);
                }
                if(temp->left){
                    q.push(temp->left);
                }
                if(temp->right){
                    q.push(temp->right);
                }
            }
        }
        
        return ans;
    }
};
