class Solution {
    public int wiggleMaxLength(int[] nums) {
        int n = nums.length;
        if(n < 2){
            return 1;
        }
        int[] incr = new int[n];
        int[] decr = new int[n];
        
        Arrays.fill(incr, 1);
        Arrays.fill(decr, 1);
        
        for(int i = 1; i < n; i++){
            for(int j = 0; j < i; j++){
                //incr 
                if(nums[i] > nums[j]){
                    incr[i] = Math.max(incr[i - 1], decr[j] + 1);
                }
                //decr 
                else if(nums[j] > nums[i]){
                    decr[i] = Math.max(decr[i - 1], incr[j] + 1);
                }
            }
        }
        return Math.max(incr[n - 1], decr[n - 1]);
        
    }
}
