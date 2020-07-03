#include<stack>
#include<queue>
class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> ans;
        vector<int> temp;
        if(root == NULL){
            return ans;
        }
        queue<TreeNode*> q;
        q.push(root);
        q.push(NULL);
        TreeNode* p;

        
        
        while(!q.empty()){
            p = q.front();
            q.pop();
            if(p == NULL){
                
                ans.push_back(temp);
                temp.clear();
                if(q.empty()){
                    break;
                }
                q.push(NULL);
            }
            else{
                temp.push_back(p->val);
                if(p->left){
                    q.push(p->left);
                }
                if(p->right){
                    q.push(p->right);
                }
            }
            
        }
        reverse(ans.begin(), ans.end());
        return ans;
        
        
    }
};