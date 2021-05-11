class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int n = cardPoints.length;
        int[] sumFront = new int[n + 1];
        int[] sumBack = new int[n + 1];
        
        sumFront[0] = sumBack[0] = 0;
        
        sumFront[1] = cardPoints[0];
        sumBack[1] = cardPoints[n - 1];
        
        for(int i = 1; i < n; i++){
            sumFront[i + 1] = sumFront[i] + cardPoints[i];
        }
        
        for(int i = 1; i < n; i++){
            sumBack[i + 1] = sumBack[i] + cardPoints[n - 1 - i];
        }
                
        int ans = 0;
        for(int i = 0; i <= k; i++){
            // i elements from front and k - i from back
            System.out.println(i + " " + sumFront[i] + " " + sumBack[k - i]);
            ans = Math.max(ans, sumFront[i] + sumBack[k - i]);
        }
        
        return ans;
    }
}
