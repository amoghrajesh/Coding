class Solution {
    public int longestOnes(int[] nums, int k) {
        int l, r;
        l = r = 0;
        int zeros = 0;
        int ans = 0;
        int windowSize = 0;
        
        while(r < nums.length){
            if(nums[r] == 0){
                zeros++;
            }
            while(zeros > k){
                if(nums[l] == 0){
                    zeros -= 1;
                }
                l++;
            }
            windowSize = r - l + 1;
            ans = Math.max(ans, windowSize);
            r++;
        }
        return ans;
    }
}
