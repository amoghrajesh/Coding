/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* p = headA;
        ListNode* q = headB;
        if(!p || !q){
            return NULL;
        }
        
        int a, b;
        a = b = 0;
        
        while(p){
            p = p->next;
            a++;
        }
        while(q){
            q = q->next;
            b++;
        }
        
        int diff = a - b;
        p = headA;
        q = headB;
        
        if(diff < 0){
            //b is bigger
            diff = -1 * diff;
            while(diff--){
                q = q->next;
            }
        }
        else if(diff > 0){
            // a is bigger
            while(diff--){
                p = p->next;
            }
        }
        while(p && q && p != q){
            p = p->next;
            q = q->next;
        }
        
        return p == q ? p : NULL;
        
    }
};
