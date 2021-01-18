class Solution {
    public int countGoodRectangles(int[][] rectangles) {
        int n = rectangles.length;
        int[] temp = new int[n];
        int m = Integer.MIN_VALUE;
        
        for(int i = 0; i < n; i++){
            temp[i] = Math.min(rectangles[i][0], rectangles[i][1]);
            if(m < temp[i]){
                m = temp[i];
            }
        }
        int ans = 0;
        for(int x: temp){
            if(x == m){
                ans++;
            }
        }
        return ans;
    }
}
