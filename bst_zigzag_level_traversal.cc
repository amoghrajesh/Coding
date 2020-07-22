#include<queue>
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if(!root){
            return ans;
        }
        queue<TreeNode*> q;
        q.push(root);
        q.push(NULL);
        TreeNode* temp;
        vector<int> level;
        
        while(!q.empty()){
            temp = q.front();
            q.pop();
            if(temp==NULL){
                ans.push_back(level);
                level.clear();
                if(q.empty()){
                    break;
                }
                q.push(NULL);
            }
            else{
                level.push_back(temp->val);
                if(temp->left){
                    q.push(temp->left);
                }
                if(temp->right){
                    q.push(temp->right);
                }
            }
        }
        
        int i = 0;
        for(vector<int> &v: ans){
            if(i%2==1){
                reverse(v.begin(), v.end());
            }
            i++;
        }
        return ans;
        
    }
};