class Solution {
    public int largestAltitude(int[] gain) {
        int height[] = new int[gain.length + 1];
        height[0] = 0;
        int m = Integer.MIN_VALUE;
        
        for(int i = 0; i < gain.length; i++){
            height[i + 1] = height[i] + gain[i];
        }
        for(int x: height){
            if(m < x){
                m = x;
            }
        }
        return m;
    }
}
