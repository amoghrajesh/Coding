class Solution {
    public boolean isIdealPermutation(int[] A) {
        int n = A.length;
        
        for(int i = 0; i < n; i++){
            int j = A[i];
            if(Math.abs(j - i) >= 2){
                return false;
            }
        }
        return true;
    }
}
