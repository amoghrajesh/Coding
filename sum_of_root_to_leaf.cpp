/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <cmath>
class Solution {
public:
    
    vector<long long long int> numbers;
    
    void printPath(long long long int* path, int n){
        long long long int temp = 0;
        for(long long long int i = 0; i < n; i++){
            temp+=path[i]*(long long long int)pow(10, n-1-i);
        }
        numbers.push_back(temp);
    }
    
    void findPath(TreeNode* root,long long long int* path,long long long int pathLen){
        if(root == NULL){
            return;
        }
        
        path[pathLen++] =  root->val;
        
        if(root->left == NULL && root->right == NULL){
            printPath(path, pathLen);
        }
        else{
            findPath(root->left, path, pathLen);
            findPath(root->right, path, pathLen);
        }
        
    }
    
    int sumNumbers(TreeNode* root) {
        numbers.clear();
        long long long int path[1000000];
        findPath(root, path, 0);
        
        int ans = 0;
        for(long long long int i = 0; i<numbers.size(); i++){
            ans+=numbers[i];
        }
        return ans;
        
    }
};