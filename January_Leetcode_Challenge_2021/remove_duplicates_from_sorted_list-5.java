class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null){
            return null;
        }
        LinkedHashMap<Integer, Integer> map= new LinkedHashMap<>();
        ListNode p = new ListNode();
        p = head;
        
        while(p != null){
            if(map.containsKey(p.val) == true){
                map.put(p.val, map.get(p.val) + 1);
            }
            else{
                map.put(p.val, 1);
            }
            p = p.next;
        }
        
        ListNode ans = null;
        ListNode h = new ListNode();
        
        for(Map.Entry<Integer, Integer> e: map.entrySet()){
            int k = e.getKey();
            int v = e.getValue();
            
            if(v == 1){
                if(ans == null){
                    ans = new ListNode();
                    ans.val = k;
                    h = ans;
                }
                else{
                    ListNode temp = new ListNode();
                    temp.val = k;
                    h.next = temp;
                    h = h.next;
                }
            }
        }
        return ans;
    }
}