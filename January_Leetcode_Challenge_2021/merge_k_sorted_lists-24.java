class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<ListNode>(
            new Comparator<ListNode>(){
                public int compare(ListNode a, ListNode b){
                    return a.val - b.val;
                }
            }
        );
        
        int k = lists.length;
        for(int i = 0; i < k; i++){
            if(lists[i] != null){
                pq.add(lists[i]);
            }
        }
        
        ListNode head = null;
        ListNode h = null;
        ListNode min;
        
        while(pq.isEmpty() == false){
            min = pq.peek();
            pq.remove();
            
            if(head == null){
                head = min;
                h = head;
            }
            else{
                h.next = min;
                h = min;
            }
            
            if(min.next != null){
                pq.add(min.next);
            }
        }
        
        return head;
    }
    
}
