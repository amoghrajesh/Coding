#include<math.h>
int getDecimalValue(struct ListNode* head){

    int ans = 0;
    struct ListNode* p = head;
    int n = 0;
    while(p!=NULL){
        n++;
        p = p->next;
    }
    
    p = head;
    n--;
    while(p!=NULL){
        if(p->val == 1){
            ans+=(int)pow(2, n);
        }
        n--;
        p = p->next;
    }
    
    return ans;
    
}