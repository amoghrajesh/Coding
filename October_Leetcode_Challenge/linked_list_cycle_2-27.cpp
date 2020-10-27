class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if(!head || !head->next){
            return NULL;
        }
        ListNode* fast;
        ListNode* slow;
        slow = fast = head;
        
        slow = slow->next;
        fast = fast->next->next;
        bool present = false;
        
        while(fast && fast->next){
            if(slow == fast){
                present = true;
                break;
            }
            slow = slow->next;
            fast = fast->next->next;
        }
        
        if(present){
            slow = head;
            while(slow != fast){
                slow = slow->next;
                fast = fast->next;
            }
            
            if(slow == fast){
                return slow;
            }
        }
        
        return NULL;
        
    }
};