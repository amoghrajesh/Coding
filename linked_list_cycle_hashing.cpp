class Solution {
public:
    bool hasCycle(ListNode *head) {
        unordered_set<ListNode*> s;
        
        ListNode* p = head;
        while(p != NULL){
            if(s.find(p) != s.end()){
                return true;
            }
            s.insert(p);
            p = p->next;
        }
        return false;
        
    }
};