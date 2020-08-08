class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;
        bool hasloop = false;
        
        while(fast && fast->next){
            slow = slow -> next;
            fast = fast -> next -> next;
            if(slow == fast){
                hasloop = true;
                break;
            }
        }
        return hasloop;
    
    }
};