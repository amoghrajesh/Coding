class Solution {
public:
    int path[1000];
    vector<int> flag;
    
    void checkSum(int n, int sum){
        int s = 0;
        for(int i = 0; i<n ;i++){
            s+=path[i];
        }
        if(s == sum){
            flag.push_back(1);
        }
        else{
            flag.push_back(0);
        }
    }
    
    void pathSum(TreeNode* root, int* path, int pathLen, int sum){
        if(root == NULL){
            return;
        }
        path[pathLen++] = root->val;
        
        if(!root->left && !root->right){
            checkSum(pathLen, sum);
        }
        
        pathSum(root->left, path, pathLen, sum);
        pathSum(root->right, path, pathLen, sum);
        
        
    }
    
    bool hasPathSum(TreeNode* root, int sum) {
        if(root == NULL){
            return false;
        }
        pathSum(root, path, 0, sum);
        for(int i = 0;i<flag.size();i++){
            if(flag[i] == 1){
                return true;
            }
        }
        return false;
    }
};