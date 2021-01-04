class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(!l1){
            return l2;
        }
        
        if(!l2){
            return l1;
        }
        
        ListNode* head = NULL;
        ListNode* h = NULL;
        
        ListNode* p, *q;
        p = l1;
        q = l2;
        int temp;
        
        while(p && q){
            if(p->val < q->val){
                temp = p->val;
                p = p->next;
            }
            else{
                temp = q->val;
                q = q->next;
            }
            
            ListNode* x = new ListNode();
            x->val = temp;
            
            if(!head){
                head = x;
                h = head;
            }
            else{
                h->next = x;
                h = h->next;
            }
        }
        
        while(p){
            ListNode* x = new ListNode();
            x->val = p->val;
            h->next = x;
            h = h->next;
            p = p->next;
            
        }
        while(q){
            ListNode* x = new ListNode();
            x->val = q->val;
            h->next = x;
            h = h->next;
            q = q->next;
            
        }
        return head;
    }
};