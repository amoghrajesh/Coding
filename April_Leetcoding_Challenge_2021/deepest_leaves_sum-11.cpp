class Solution {
public:
    int ans = 0;
    int maxDepth(TreeNode* root){
        if(!root){
            return 0;
        }
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }
    
    void traverse(TreeNode* root, int level, int depth){
        if(!root){
            return;
        }
        if(level == depth){
            ans += root->val;
        }
        traverse(root->left, level + 1, depth);
        traverse(root->right, level + 1, depth);
    }
    
    int deepestLeavesSum(TreeNode* root) {
        if(!root){
            return 0;
        }
        
        int depth = maxDepth(root);
        int level = 0;
        traverse(root, level, depth - 1);
        
        return ans;
    }
};
