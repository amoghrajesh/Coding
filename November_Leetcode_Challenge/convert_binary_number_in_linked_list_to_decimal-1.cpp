class Solution {
public:
    int getDecimalValue(ListNode* head) {
        int n = 0;
        ListNode* p = head;
        if(!p){
            return n;
        }
        
        while(p){
            p = p->next;
            n++;
        }
        
        p = head;
        int ans = 0;
        while(p){
            ans += ((int)pow(2, --n) * p->val);
            p = p->next;
        }
        
        return ans;
        
    }
};