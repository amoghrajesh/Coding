class Solution {
public:
    int path[1000];
    int sum;
    
    void findSum(int n){
        for(int i = 0;i<n;i++){
            sum += ((1<<(n-1-i))*path[i]);
        }
    }
    
    void pathSum(TreeNode* root, int* path, int pathLen){
        if(!root){
            return;
        }
        
        path[pathLen++] = root->val;
        if(!root->left && !root->right){
            findSum(pathLen);
        }
        pathSum(root->left, path, pathLen);
        pathSum(root->right, path, pathLen);
    }
    
    int sumRootToLeaf(TreeNode* root) {
        if(root == NULL){
            return 0;
        }
        sum = 0;
        pathSum(root, path, 0);
        return sum;
    }
};