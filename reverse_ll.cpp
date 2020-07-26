class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(!head || !head->next){
            return head;
        }
        if(!head->next->next){
            ListNode* p = head -> next;
            p->next = head;
            head->next = NULL;
            return p;
        }
        
        ListNode* p = head;
        ListNode* q = head->next;
        ListNode* r = head->next->next;
        p->next = NULL;
        

        while(r){
            q->next = p;
            p = q;
            q = r;
            r = r->next;
        }
        q->next = p;
        p = q;
        return p;
        
    }
};