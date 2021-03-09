class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int v, int d) {
        if(d == 1){
            TreeNode* temp = new TreeNode(v);
            temp->left = root;
            return temp;
        }
        
        queue<TreeNode*> q;
        q.push(root);
        int depth = 1;
        TreeNode* temp;
        int size;
        
        while(depth <= d - 2){
            size = q.size();
            while(size--){
                temp = q.front();
                q.pop();
                
                if(temp->left){
                    q.push(temp->left);
                }
                if(temp->right){
                    q.push(temp->right);
                }
            }
            depth++;
        }
        
        TreeNode* node;
        TreeNode* prev;
        
        while(!q.empty()){
            temp = q.front();
            q.pop();
            node = new TreeNode(v);
            prev = temp->left;
            temp->left = node;
            node->left = prev;
            
            node = new TreeNode(v);
            prev = temp->right;
            temp->right = node;
            node->right = prev;
        }
        
        return root;
    }
};
