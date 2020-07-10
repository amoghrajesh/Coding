#include<stack>
class Solution {
public:
    Node* flatten(Node* head) {
        if(!head){
            return head;
        }
        
        vector<int> data;
        stack<Node*> s;
        s.push(head);
        Node* temp;
        
        while(!s.empty()){
            temp = s.top();
            s.pop();
            data.push_back(temp->val);
            if(temp->next){
                s.push(temp->next);
            }
            if(temp->child){
                s.push(temp->child);
            }
        }
        
        Node* h = new Node();
        h->val = data[0];
        h->next = h->prev = h->child = NULL;
        
        temp = h;
        int x = data.size();
        int i = 1;
        
        while(i<x){
            Node* y = new Node();
            y->val = data[i];
            y->next = y->prev = y->child = NULL;
            temp->next = y;
            y->prev = temp;
            temp = temp -> next;
            i++;
        }
        return h;

    }
};