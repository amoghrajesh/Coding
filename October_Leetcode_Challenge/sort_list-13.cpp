class Solution {
public:
    ListNode* split(ListNode* head){
        ListNode* fast = head->next;
        ListNode* slow = head;
        
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        
        return slow;
    }
    
    ListNode* merge(ListNode* a, ListNode* b){
        if(!a){
            return b;
        }
        
        if(!b){
            return a;
        }
        ListNode* res;
        if(a->val <= b->val){
            res = a;
            res->next = merge(a->next, b);
        }
        else{
            res = b;
            res->next = merge(a, b->next);
        }
        return res;
        
    }
    
    ListNode* sortList(ListNode* head) {
        if(!head || !head->next){
            return head;
        }
        
        ListNode* mid = split(head);
        
        ListNode* p1 = head;
        ListNode* p2 = mid->next;
        
        mid->next = NULL;
        p1 = sortList(p1);
        p2 = sortList(p2);
        
        ListNode* h = merge(p1, p2);
        return h;
        
    }
};