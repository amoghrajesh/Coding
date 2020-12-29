class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> q =  new PriorityQueue<Integer>(Collections.reverseOrder());
        for(int x: stones){
            q.add(x);
        }
        int y, x;
        while(q.size() > 1){
            y = q.poll();
            x = q.poll();
            if(y >= x){
                q.add(y - x);
            }
        }
        
        return q.size() == 0 ? 0 : q.poll();
        
    }
}