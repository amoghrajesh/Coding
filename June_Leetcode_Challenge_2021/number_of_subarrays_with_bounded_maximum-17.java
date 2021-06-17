class Solution {
    public int numSubarrayBoundedMax(int[] nums, int left, int right) {
        int start = 0, n = nums.length, count = 0;
        int subArrLenTillNow = 0;
        for (int i = 0; i < n; i++) {
            
            
            if (nums[i] < left) {
                
                count = count + subArrLenTillNow;  // Not single element subarray, Part of subarray
                
            } else if (nums[i] >= left && nums[i] <= right) {
                
                subArrLenTillNow = i - start + 1;
                count = count + subArrLenTillNow;   // Single element subarray, Part of subarray
                
            } else {
             
                start = i + 1;   // Not single element subarray, Not part of subarray
                subArrLenTillNow = 0;
                
            }
            
            
        }
        
        return count;
    }
}
