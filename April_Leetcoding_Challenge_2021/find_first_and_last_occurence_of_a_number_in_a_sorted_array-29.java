class Solution {
    public int BS(int[] nums, int l, int r, int target, int flag){
        int ans = -1;
        int m;
        
        while(l <= r){
            m = (l + r) / 2;
            if(nums[m] < target){
                l = m + 1;
            }
            else if(nums[m] > target){
                r = m - 1;
            }
            else{
                ans = m;
                if(flag == 0){
                    r = m - 1;
                }
                else{
                    l = m + 1;
                }
            }
        }
        return ans;
    }
    
    public int[] searchRange(int[] nums, int target) {
        int n = nums.length;
        
        int first = BS(nums, 0, n - 1, target, 0);
        int last = BS(nums, 0, n - 1, target, 1);
        
        
        int[] ans = new int[2];
        ans[0] = first; ans[1] = last;
        
        return ans;
    }
}
