class Solution {
    public int[] fairCandySwap(int[] A, int[] B) {
        int a = A.length;
        int b = B.length;
        int sa = 0, sb = 0;
        
        for(int i: A){
            sa += i;
        }
        
        for(int i: B){
            sb += i;
        }
        
        int ans[] = new int[2];
        int x, y;
        
        for(int i = 0; i < a; i++){
            x = A[i];
            for(int j = 0; j < b; j++){
                y = B[j];
                if(sa - x + y == sb - y + x){
                    ans[0] = x;
                    ans[1] = y;
                    break;
                }
            }
        }
        return ans;
    }
}