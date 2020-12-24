class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(!head || !head->next){
            return head;
        }
        ListNode* prev = head;
        ListNode* curr = head->next;
        head = curr;
        
        while(1){
            ListNode* next = curr->next;
            curr->next = prev;
            
            if(!next || !next->next){
                prev->next = next;
                break;
            }
            
            prev->next = next->next;
            
            prev = next;
            curr = prev->next;
        }
        return head;
        
    }
};