class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if(!l1){
            return l2;
        }
        if(!l2){
            return l1;
        }
        
        ListNode* p = l1;
        ListNode* q = l2;
        int m = 0, n = 0;
        
        while(p){
            m++;
            p = p->next;
        }
        
        while(q){
            n++;
            q = q->next;
        }
        
        p = l1;
        q = l2;
        int sum = 0;
        int c = 0;
        ListNode* ans = NULL;
        ListNode* a;
        
        while(p && q){
            sum = (p->val + q->val) + c;
            c = sum / 10;
            sum %= 10;
            
            if(!ans){
                ans = new ListNode();
                ans->val = sum;
                a = ans;
            }
            else{
                ListNode* temp = new ListNode();
                temp->val = sum;
                a->next = temp;
                a = a->next;
            }
            
            p = p->next;
            q = q->next;
            
        }
        
        while(p){
            sum = (p->val) + c;
            c = sum / 10;
            sum %= 10;
            
            ListNode* temp = new ListNode();
            temp->val = sum;
            a->next = temp;
            a = a->next;
            
            p = p->next;
            
        }
        while(q){
            sum = (q->val) + c;
            c = sum / 10;
            sum %= 10;
            
            ListNode* temp = new ListNode();
            temp->val = sum;
            a->next = temp;
            a = a->next;
            
            q = q->next;
            
        }
        
        if(c == 1){
            ListNode* temp = new ListNode();
            temp->val = c;
            a->next = temp;
            a = a->next;
        }
        
        return ans;
        
    }
};