class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* p = headA;
        ListNode* q = headB;
        int n1 = 0;
        int n2 = 0;
        while(p){
            p = p->next;
            n1++;
        }
        while(q){
            q = q->next;
            n2++;
        }
        if(n1 == 0 || n2 == 0){
            return NULL;
        }
        p = headA;
        q = headB;
        int d;
        if(n1 > n2){
            d = n1 - n2;
            while(d--){
                p = p->next;
            }
        }
        else{
            d = n2 - n1;
            while(d--){
                q = q -> next;
            }
        }
        
        //same pos now
        while(p && q){
            if(p == q){
                return p;
            }
            p = p-> next;
            q = q -> next;
        }
        return NULL;
        
    }
};