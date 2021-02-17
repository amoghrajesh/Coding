class Solution {
    public int maxArea(int[] height) {
        int l = 0;
        int n = height.length;
        int r = n - 1;
        int capacity = Integer.MIN_VALUE;
        int m;
        
        while(l < r){
            capacity = Math.max(capacity, (r - l) * Math.min(height[l], height[r]));
            m = Math.min(height[l], height[r]);
            
            if(m == height[l]){
                l++;
            }
            else{
                r--;
            }
        }
        return capacity;
    }
}
