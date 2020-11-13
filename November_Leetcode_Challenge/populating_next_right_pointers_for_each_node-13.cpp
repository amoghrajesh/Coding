#include<queue>
class Solution {
public:
    Node* connect(Node* root) {
        if(!root){
            return NULL;
        }
        
        queue<Node*> q;
        q.push(root);
        q.push(NULL);
        Node* temp;
        
        while(!q.empty()){
            temp = q.front();
            q.pop();
            
            if(!temp){
                if(q.empty()){
                    break;
                }
                q.push(NULL);
            }
            else{
                temp->next = q.front();
                if(temp->left){
                    q.push(temp->left);
                }
                if(temp->right){
                    q.push(temp->right);
                }
            }
        }
        
        return root;
    }
};