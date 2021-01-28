class Solution {
    public String getSmallestString(int n, int k) {
        char[] ans = new char[n];
        Arrays.fill(ans, 'a');
        int index = 0;
        
        for(int i = n - 1; i > -1; i--){
            k -= i;
            if(k < 0){
                break;
            }
            if(k >= 26){
                ans[i] = 'z';
                k -= 26;
            }
            else{
                index = k + 96;
                char x = (char)(index);
                ans[i] = x;
                k -= (index - 96);
            }
            k += i;
        }
        return new String(ans);
        
    }
}
