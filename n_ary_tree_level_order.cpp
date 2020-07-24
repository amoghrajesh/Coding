#include<queue>
class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> ans;
        if(!root){
            return ans;
        }
        queue<Node*> q;
        q.push(root);
        q.push(NULL);
        Node* temp;
        vector<int> level;
        
        while(!q.empty()){
            temp = q.front();
            q.pop();
            
            if(temp==NULL){
                ans.push_back(level);
                level.clear();
                if(q.empty()){
                    break;
                }
                q.push(NULL);
            }
            else{
                level.push_back(temp->val);
                for(int i = 0; i<temp->children.size(); i++){
                    if(temp->children[i]){
                        q.push(temp->children[i]);
                    }
                }
            }
        }
        return ans;
    }
};