#include <stack>
class Solution {
public:
    void reorderList(ListNode* head) {
        if(!head){
            return;
        }
        if(!head->next){
            return;
        }
        
        ListNode* p = head;
        ListNode* q;
        int n = 0;
        while(p){
            n++;
            p = p -> next;
        }
        int mid = n / 2 ;
        
        p = head;
        while(mid--){
            q = p;
            p = p -> next;
        }
        q->next = NULL;
        stack<ListNode*> s;
        while(p){
            s.push(p);
            p = p -> next;
        }
        
        p = head;
        ListNode* temp;
        
        
        while(p && !s.empty()){
            temp = s.top();
            s.pop();
            
            temp->next = p->next;
            p->next = temp;
            if(!p->next->next){
                q = p->next;
            }
            p = p->next->next; 
            
            
        }
        
        if(!s.empty()){
            temp = s.top();
            s.pop();
            q->next = temp;
            temp->next = NULL;
        }
         
        return; 
    }
};