class Solution {
    public int maxOperations(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int x: nums){
            if(map.containsKey(x)){
                map.put(x, map.get(x) + 1);
            }
            else{
                map.put(x, 1);
            }
        }
        int ans = 0;
        
        for(int x: nums){
            if(map.get(x) >= 1 && map.containsKey(k - x) && map.get(k - x) >= 1){
                map.put(x, map.get(x) - 1);
                if(map.get(k - x) < 1){
                    continue;
                }  
                map.put(k - x, map.get(k - x) - 1);
                ans++;
            }
        }
        return ans;
    }
}
