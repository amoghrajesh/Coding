class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int w = wall.size();
        
        for(List<Integer> row: wall){
            int n = row.size();
            int c = 0;
            for(int i = 0; i < n - 1; i++){
                c += row.get(i);
                if(map.containsKey(c) == true){
                    map.put(c, map.get(c) + 1);
                }
                else{
                    map.put(c, 1);
                }
            }
        }
        
        int max = Integer.MIN_VALUE;
        for (int key: map.keySet()) {
            max = Math.max(max, map.get(key));
        }
        
        return max == Integer.MIN_VALUE ? w : w - max;
    }
}
