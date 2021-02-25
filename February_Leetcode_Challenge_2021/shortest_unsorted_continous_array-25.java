class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int n = nums.length;
        int[] temp = new int[n];
        
        for(int i = 0; i < n; i++){
            temp[i] = nums[i];
        }
        
        int left = Integer.MAX_VALUE;
        int right = Integer.MIN_VALUE;
        boolean isNotSorted = true;
        
        Arrays.sort(temp);
        for(int i = 0; i < n; i++){
            if(nums[i] != temp[i]){
                isNotSorted = false;
                if(left == Integer.MAX_VALUE){
                    left = i;
                }
                right = Math.max(right, i);
            }
        }
        return isNotSorted == false ? right - left + 1 : 0;
        
    }
}
