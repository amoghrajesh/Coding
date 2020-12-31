class Solution {
    public int countNegatives(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int l, r, mid;
        int ans = 0;
        
        for(int i = 0; i < n; i++){
            l = 0;
            r = m;
            mid = -1;
            while(l < r){
                mid = (l + r)/2;
                // System.out.println(mid);
                if(grid[i][mid] >= 0){
                    l = mid + 1;
                }
                else{
                    r = mid;
                }
            }
            // System.out.println(mid);
            if(mid != -1){
                ans += (m - l);
            }
        }
        return ans;
    }
}