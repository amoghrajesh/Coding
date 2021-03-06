/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void inOrder(struct TreeNode* root, int* flag)
{
    if(root!=NULL){
        inOrder(root->left, flag);
        flag[root->val] = 1;
        inOrder(root->right, flag);
    }
}

bool isUnivalTree(struct TreeNode* root){

    int flag[100];
    for(int i=0;i<100;i++){
        flag[i] = 0;
    }
    inOrder(root, flag);

    int c = 0;
    for(int i=0;i<100;i++){
        if(flag[i]==1){
            c++;
        }
    }

    if(c==1){
        return true;
    }
    return false;


}