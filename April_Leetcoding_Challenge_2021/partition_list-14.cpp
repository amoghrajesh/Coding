/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        vector<int> nodes;
        ListNode* p = head;
        while(p){
            if(p->val < x){
                nodes.push_back(p->val);
            }
            p = p->next;
        }
        
        p = head;
        while(p){
            if(p->val >= x){
                nodes.push_back(p->val);
            }
            p = p->next;
        }
        
        ListNode* h = NULL;
        
        for(int val: nodes){
            if(!h){
                ListNode* temp = new ListNode(val);
                h = temp;
                p = h;
            }
            else{
                ListNode* temp = new ListNode(val);
                p->next = temp;
                p = temp;
            }
        }
        
        return h;
    }
};
