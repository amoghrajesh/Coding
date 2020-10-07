class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        ListNode* p = head;
        ListNode* q;
        
        if(!head || !k){
            return head;
        }
        
        if(!head->next){
            return head;
        }
        
        int n = 0;
        while(p){
            n++;
            p = p->next;
        }
        
        p = head;
        k %= n;
        k = n - k;
        
        if(k == n){
            return head;
        }
        
        while(k){
            q = p;
            p = p->next;
            k--;
        }
        q->next = NULL;
        ListNode* h = p;
        ListNode* r;
        // return h;
        while(p){
            r = p;
            p = p->next;
        }
        r->next = head;
        head = h;
        return head;
 
    }
};