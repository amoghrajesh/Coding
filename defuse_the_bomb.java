class Solution {
    public int[] decrypt(int[] code, int k) {
        int n = code.length;
        int[] ans = new int[n];
        if(k == 0){
            return ans;
        }
        else if(k > 0){
            int c = 0;
            int j;
            int temp;
            for(int i = 0; i < n; i++){
                j = (i == n - 1 ? 0 :i + 1);
                temp = 0;
                c = 0;
                while(c < k){
                    temp += code[j];
                    j = (j + 1) % n;
                    c++;
                }
                ans[i] = temp;
            }
        }
        else{
            int j, temp;
            for(int i = 0; i < n; i++){
                j = (i + n - (-1 * k)) % n;
                temp = 0;
                while(j != i){
                    temp += code[j];
                    j = (j + 1) % n;
                }
                ans[i] = temp;
            }
        }
        return ans;
    }
}