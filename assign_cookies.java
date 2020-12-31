class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        
        int nchildren = g.length;
        int ncookies = s.length;
        int child;
        int ans = 0;
        int j = 0;
        
        for(int i = 0; i < nchildren; i++){
            child = g[i];
            while(j < ncookies){
                if(s[j] >= child){
                    ans++;
                    j++;
                    break;
                }
                j++;
            }
            if(j == ncookies){
                return ans;
            }
        }
        return ans;
    }
}