#include<stack>
class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> ans;
        if(!root){
            return ans;
        }
        stack<Node*> s;
        s.push(root);
        Node* temp;
        
        while(!s.empty()){
            temp = s.top();
            s.pop();
            ans.push_back(temp->val);
            
            for(int i = temp->children.size() - 1; i > -1; i--){
                s.push(temp->children[i]);
            }
        }
        return ans;
    }
};
