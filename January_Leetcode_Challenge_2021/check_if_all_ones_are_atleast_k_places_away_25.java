class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        int n = nums.length;
        List<Integer> ones = new ArrayList<>();
        
        for(int i = 0; i < n; i++){
            if(nums[i] == 1){
                ones.add(i);
            }
        }
        
        for(int i = 0; i < ones.size() - 1; i++){
            if(ones.get(i + 1) - ones.get(i) <= k){
                return false;
            }
        }
        
        return true;
    }
}
