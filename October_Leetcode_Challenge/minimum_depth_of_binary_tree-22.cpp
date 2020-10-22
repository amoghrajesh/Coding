#include<queue>
class Solution {
public:
    bool isleaf(TreeNode* node){
        return !node->left && !node->right;
    }
    
    int minDepth(TreeNode* root) {
        if(!root){
            return 0;
        }
        queue<TreeNode*> q;
        q.push(root);
        q.push(NULL);
        
        vector<vector<TreeNode*>> levels;
        vector<TreeNode*> level;
        TreeNode* temp;
        
        while(!q.empty()){
            temp = q.front();
            q.pop();
            
            if(!temp){
                levels.push_back(level);
                level.clear();
                if(q.empty()){
                    break;
                }
                q.push(NULL);
            }
            else{
                if(isleaf(temp)){
                    return levels.size() + 1;
                }
                level.push_back(temp);
                if(temp->left){
                    q.push(temp->left);
                }
                if(temp->right){
                    q.push(temp->right);
                }
            }
            
        }
        
        return levels.size() + 1;
    }
};