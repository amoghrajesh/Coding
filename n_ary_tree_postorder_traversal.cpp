#include <stack>
class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> ans;
        if(!root){
            return ans;
        }
        stack<Node*> s1, s2;
        Node* temp;
        s1.push(root);
        
        while(!s1.empty()){
            temp = s1.top();
            s1.pop();
            for(Node* n: temp->children){
                s1.push(n);
            }
            s2.push(temp);
        }
        while(!s2.empty()){
            temp = s2.top();
            ans.push_back(temp->val);
            s2.pop();
        }
        return ans;
    }
};