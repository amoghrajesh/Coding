#include<queue>
class Codec {
public:
    string enc = "";
    queue<TreeNode*> q;
    
    TreeNode* newNode(int data){
        TreeNode* n = new TreeNode(data);
        // n->val = data;
        n->left = n->right = NULL;
        return n;
    }
    
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if(!root){
            return enc;
        }
        enc += to_string(root->val);
        q.push(root);
        TreeNode* temp;
        while(!q.empty()){
            temp = q.front();
            q.pop();
            if(!temp){
                break;
            }
            enc += (temp->left == NULL ? "#" : to_string(temp->left->val));
            enc += (temp->right == NULL ? "#" : to_string(temp->right->val));
            if(temp->left){
                q.push(temp->left);
            }
            else{
                q.push(NULL);
            }
            
            
            if(temp->right){
                q.push(temp->right);
            }
            else{
                q.push(NULL);
            }
        }
        return enc;
        
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        TreeNode* n = q.front();
        q.pop();
        if(!n){
            return NULL;
        }
        // TreeNode* n = temp;
        n->left = deserialize(data);
        n->right = deserialize(data);
        return n;
    }
};
