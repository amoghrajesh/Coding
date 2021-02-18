class Solution {
    public boolean isAP(int[] A, int curr, int prev, int old){
        return A[curr] - A[prev] == A[prev] - A[old];
    }
    public int numberOfArithmeticSlices(int[] A) {
        int n = A.length;
        if(n <= 1){
            return 0;
        }
        
        int[] dp = new int[n];
        dp[0] = dp[1] = 0;
        
        for(int i = 2; i < n; i++){
            if(isAP(A, i, i - 1, i - 2) == true){
                dp[i] = 1 + dp[i - 1];
            }
        }
        
        return Arrays.stream(dp).sum();
    }
}
