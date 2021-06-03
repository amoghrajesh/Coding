class Solution {
    public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        int hGap, vGap;
        int m = horizontalCuts.length;
        int n = verticalCuts.length;
        Arrays.sort(horizontalCuts);
        Arrays.sort(verticalCuts);
        
        hGap = Math.max(horizontalCuts[0], h - horizontalCuts[m - 1]);
        vGap = Math.max(verticalCuts[0], w - verticalCuts[n - 1]);
        
        for(int i = 1; i < m; i++){
            hGap = Math.max(horizontalCuts[i] - horizontalCuts[i - 1], hGap);
        }
        
        for(int i = 1; i < n; i++){
            vGap = Math.max(verticalCuts[i] - verticalCuts[i - 1], vGap);
        }
        
        return (int) ((long)hGap * vGap % 1000000007);
        
    }
}
