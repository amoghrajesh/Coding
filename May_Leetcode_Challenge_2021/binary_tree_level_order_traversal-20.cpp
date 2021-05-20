class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if(!root){
            return ans;
        }
        queue<TreeNode*> q;
        q.push(root);
        q.push(NULL);
        vector<int> level;
        TreeNode* temp;
        
        while(!q.empty()){
            temp = q.front();
            q.pop();
            
            if(temp == NULL){
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
        return ans;
    }
};
