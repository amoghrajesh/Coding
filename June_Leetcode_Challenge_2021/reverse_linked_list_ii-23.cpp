class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode *h = new ListNode(0, head);
        ListNode* cur = h;
        ListNode* prev = NULL;
        
        for(int i = 0; i < left; i++){
            prev = cur;
            cur = cur->next;
        }
        
        ListNode* p1 = prev;
        ListNode* p2 = cur;
        ListNode* temp;
        
        for(int i = left; i < right + 1; i++){
            temp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = temp;
        }
        
        p1->next = prev;
        p2->next = cur;
        
        return h->next;
    }
};
