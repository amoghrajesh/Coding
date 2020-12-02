#include <cstdlib>
#include <ctime>
class Solution {
public:
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    vector<int> v;
    
    Solution(ListNode* head) {
        ListNode* p = head;
        
        while(p != NULL){
            v.push_back(p->val);
            p = p->next;
        }

    }
    
    /** Returns a random node's value. */
    int getRandom() {
        int n = v.size();
        int index = (rand() % n);
        
        return v[index];
    }
};