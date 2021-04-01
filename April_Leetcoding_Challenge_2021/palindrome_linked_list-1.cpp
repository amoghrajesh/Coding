class Solution {
public:
    bool isPalindrome(ListNode* head) {
        vector<int> list;
        ListNode* p = head;
        while(p){
            list.push_back(p->val);
            p = p->next;
        }
        
        int n = list.size();
        for(int i = 0; i < n / 2; i++){
            if(list[i] != list[n - 1 - i]){
                return false;
            }
        }
        return true;
    }
};
