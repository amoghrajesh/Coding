#include<cmath>
class Solution {
public:
    int ans = 0;
    
    int traverse(TreeNode* root){
        if(!root){
            return 0;
        }
        
        int l = traverse(root->left);
        int r = traverse(root->right);
        
        int tilt = abs(r - l);
        
        ans += tilt;
        
        return root->val + l + r;
        
    }
    
    int findTilt(TreeNode* root) {
        traverse(root);
        return ans;
    }
};