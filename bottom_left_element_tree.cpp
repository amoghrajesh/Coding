#include<queue>
#include<algorithm>
class Solution {
public:
    
    int height(TreeNode* root){
        if(!root){
            return 0;
        }
        
        return 1 + max(height(root->left), height(root->right));
    }
    
    int findBottomLeftValue(TreeNode* root) {
        int h = height(root);
        queue<TreeNode*> q;
        q.push(root);
        q.push(NULL);
        TreeNode* temp;
        vector<int> last;
        int level = 1;
        vector<vector<int>> ans;
        
        while(!q.empty()){
            temp = q.front();
            q.pop();
            
            if(temp == NULL){
                level++;
                if(level == h + 1){
                    break;
                }
                q.push(NULL);
                last.clear();
            }
            else{
                last.push_back(temp->val);
                if(temp->left){
                    q.push(temp->left);
                }
                if(temp->right){
                    q.push(temp->right);
                }
            }
            
        }
        return last[0];
        
        
    }
};