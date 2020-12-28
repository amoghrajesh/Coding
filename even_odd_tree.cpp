class Solution {
public:
    bool isEvenOddTree(TreeNode* root) {
        queue<TreeNode*> myQueue;
        
        TreeNode* cur = root;
        myQueue.push(cur);
        int index = 0;
        while(myQueue.size()!=0){
            int size = myQueue.size();
            int pre = -1;
            for(int i=0;i<size;i++){
                TreeNode* node = myQueue.front();

                if(index%2==0 && (node->val%2==0 || (i>0 && node->val<=pre))){
                    return false;
                }
                if(index%2==1 && (node->val%2==1 || (i>0 && node->val>=pre))){
                    return false;
                }
                
                pre = node->val;
                myQueue.pop();
                if(node->left!=nullptr){
                    myQueue.push(node->left);
                }
                if(node->right!=nullptr){
                    myQueue.push(node->right);
                }
            }
            index++;
        }
        
        
        return true;
    }
};