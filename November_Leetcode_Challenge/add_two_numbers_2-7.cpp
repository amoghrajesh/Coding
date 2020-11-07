class Solution {
public:
    int getLength(ListNode* l) {
        ListNode * ptr = l;
        int length = 0;
        while(ptr){
            length++;
            ptr = ptr->next;
        }
        return length;
    }
    ListNode* reverese(ListNode* l){
        ListNode* curr= l;
        ListNode* next = NULL;
        ListNode* prev = NULL;
        while(curr){
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int n1 = getLength(l1);
        int n2 = getLength(l2);
        
        ListNode* ptr1 = l1;
        ListNode* ptr2 = l2;
        int val1, val2;
        
        //add aligning digits regardless of carry
        ListNode * sum = NULL;
        for(int i = max(n1,n2); i > 0; i--){
            val1 = 0;
            val2 = 0;
            if(i <= n1){
                val1 = ptr1->val;
                ptr1 = ptr1->next;
            }
            if( i <= n2){
                val2 = ptr2->val;
                ptr2 = ptr2->next;
            }
            ListNode * new_node = new ListNode(val1 + val2);
            new_node->next = sum;
            sum = new_node;    
        }
        // check carry
        ListNode *sum_ptr = sum;
        int carry = 0;
        while(sum_ptr){
                int digit = sum_ptr->val + carry;
                sum_ptr->val = digit % 10;
                carry = digit / 10;
                sum_ptr = sum_ptr->next;
        }
        sum = reverese(sum);
        if(carry){
            ListNode* new_node = new ListNode(carry);
            new_node->next = sum;
            sum = new_node;
        }
        return sum;
    }
};