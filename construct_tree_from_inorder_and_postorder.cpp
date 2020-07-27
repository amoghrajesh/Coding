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
#include <unordered_map>
class Solution {
public:
    TreeNode* newNode(int data){
        TreeNode* node = new TreeNode();
        node->val = data;
        node->left = node->right = NULL;
        return node;
    }
    
    TreeNode* buildUtil(vector<int>& inorder, vector<int>& postorder, int start, int end, int* postIndex, unordered_map<int, int> map){
        
        if(start > end){
            return NULL;
        }
        
        int val = postorder[*postIndex];
        (*postIndex)--;
        TreeNode* node = newNode(val);
        
        
        if(start == end){
            return node;
        }
        
        int inIndex = map[val];
        
        node->right = buildUtil(inorder, postorder, inIndex + 1, end, postIndex, map);
        node->left = buildUtil(inorder, postorder, start, inIndex - 1, postIndex, map);
        
        return node;
   
    }
    
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        unordered_map<int, int> map;
        for(int i = 0; i< inorder.size(); i++){
            map[inorder[i]] = i;
        }
        int postIndex = inorder.size() - 1;
        return buildUtil(inorder, postorder, 0, inorder.size() - 1, &postIndex, map);
    }
};