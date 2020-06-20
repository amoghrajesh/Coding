#include<queue>
class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        
        queue<TreeNode*> q;
        q.push(root);
        q.push(NULL);
        int lsum = 0;
        int j = 0;
        TreeNode* temp;
        int ans = INT_MIN;
        int level = 0;
        
        while(!q.empty()){
            temp = q.front();
            q.pop();
            if(q.empty()){
                break;
            }
            if(temp != NULL){
                lsum += temp->val;
                if(temp->left){
                    q.push(temp->left);
                }
                if(temp->right){
                    q.push(temp->right);
                }
            }
            else{  
                j++;
                if(lsum > ans){
                    ans = lsum;
                    level = j;
                }
                q.push(NULL);
                lsum  = 0;
            }
            
        }
        return level; 
    }
};