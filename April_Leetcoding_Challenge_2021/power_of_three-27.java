class Solution {
    public boolean isPowerOfThree(int n) {
        // int maxValue = 0;
        // while(maxValue < (int) Math.pow(2, 31)){
        //     maxValue += 3;
        // }
            
        return n <= 0 ? false : 1162261467 % n == 0; 
    }
}
