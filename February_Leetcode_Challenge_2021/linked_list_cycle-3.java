public class Solution {
    public boolean hasCycle(ListNode head) {
        if(head == null){
            return false;
        }
        ListNode hare, tortoise;
        tortoise = hare = head;
        
        while(tortoise.next != null && hare.next != null && hare.next.next != null){
            tortoise = tortoise.next;
            hare = hare.next.next;
            if(tortoise == hare){
                return true;
            }
        }
        return false;
        
    }
}
