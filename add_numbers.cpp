class Solution {
public:
    ListNode* newNode(int data){
        ListNode* node = new ListNode();
        node -> val = data;
        node -> next = NULL;
        return node;
    }
    
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* p = l1;
        ListNode* q = l2;
        if(!p){
            return q;
        }
        if(!q){
            return p;
        }
        
        int sum = 0;
        int carry = 0;
        ListNode* head = NULL;
        ListNode* h;
        
        while(p && q){
            sum = carry + (p->val) + (q->val);
            p = p -> next;
            q = q -> next;
            carry = (sum >= 10) ? 1: 0;
            
            sum = sum % 10;
            if(head == NULL){
                head = newNode(sum);
                h = head;
            }
            else{
                head -> next = newNode(sum);
                head = head->next;
            }
        }
        
        while(p){
            sum = carry + (p->val);
            p = p->next;
            carry = (sum >= 10) ? 1: 0;
            sum = sum % 10;
            head -> next = newNode(sum);
            head = head->next;
        }
        
        while(q){
            sum = carry + (q->val);
            q = q->next;
            carry = (sum >= 10) ? 1: 0;
            sum = sum % 10;
            head -> next = newNode(sum);
            head = head->next;
        }
        if(carry > 0){
            head->next = newNode(1);
            head = head->next;
        }
        return h;
        
    }
};