class Solution {
    public int minOperations(int n) {
        int target = (n * n) / n;
        int ans = 0;
        
        for(int i = 0; i < n / 2; i++){
            ans += (target - (2 * i + 1));
        }
        return ans;
    }
}
