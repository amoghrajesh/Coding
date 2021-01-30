class Solution {
    public int[] decompressRLElist(int[] nums) {
        ArrayList<Integer> ans = new ArrayList<>();
        int n = nums.length;
        int f, v;
        
        for(int i = 0; i < n / 2; i++){
            f = nums[2 * i];
            v = nums[2 * i + 1];
            
            for(int j = 0; j < f; j++){
                ans.add(v);
            }
        }
        int[] res = ans.stream().mapToInt(i -> i).toArray();
        return res;
    }
}