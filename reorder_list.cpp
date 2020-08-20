class Solution {
public:
    void reorderList(ListNode* head) {
        if(!head){
            return;
        }
        
        ListNode* cur = head;
        ListNode* last;
        ListNode* p;
        while(cur){
            last = cur;
            p = cur;
            while(last->next && last->next->next){
                last = last -> next;
            }
            p = last -> next;
            last->next = NULL;
            if(!p){
                break;
            }
            p->next = cur->next;
            cur->next = p;
            cur = cur->next->next; 
        }
        return;
        
    }
};