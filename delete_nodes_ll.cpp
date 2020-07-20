class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode s(0); 
        s.next = head;
        ListNode *cur = head, *prev = &s;
        while(cur) {
            if(cur->val == val)
                prev->next = cur->next;
            else
                prev = cur;
            cur = cur->next;
        }
        return s.next;
    }
};