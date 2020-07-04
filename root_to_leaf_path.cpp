#include<string>
class Solution {
public:
    
    int path[1000];
    vector<string> ans;
    
    void printArr(int n){
        string temp = "";
        for(int i = 0;i<n-1;i++){
            temp = temp + to_string(path[i]);
            temp = temp + "->";
        }
        temp = temp + to_string(path[n-1]);
        ans.push_back(temp);
        
    }
    
    void printPath(TreeNode* root, int* path, int pathLen){
        if(root == NULL){
            return;
        }
        
        path[pathLen] = root->val;
        pathLen++;
        
        if(root -> left == NULL && root -> right == NULL){
            printArr(pathLen);
        }
        
        printPath(root->left, path, pathLen);
        printPath(root->right, path, pathLen);
        
        
    }
    
    vector<string> binaryTreePaths(TreeNode* root) {
        ans.clear();
        printPath(root, path, 0);
        return ans;
    }
};