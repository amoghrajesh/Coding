class Solution {
public:
    int maxDepth(Node* root) {
        int level = 0;
        if(!root){
            return level;
        }
        queue<Node*> q;
        int size = 0;
        Node* temp;
        q.push(root);
        
        while(!q.empty()){
            size = q.size();
            while(size--){
                temp = q.front();
                q.pop();
                
                for(auto child: temp->children){
                    q.push(child);
                }
            }
            level++;
        }
        return level;
    }
};