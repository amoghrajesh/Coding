class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        ListNode p = head;
        int n = 0;
        while(p != null){
            p = p.next;
            n++;
        }
        p = head;
        ListNode x1 = head;
        ListNode x2 = head;
        
        int counter = 1;
        while(p != null){
            if(counter == k){
                x1 = p;
            }
            if(counter == (n - k + 1)){
                x2 = p;
            }
            p = p.next;
            counter++;
        }
        int temp = x1.val;
        x1.val = x2.val;
        x2.val = temp;
        
        return head;
        
    }
}
