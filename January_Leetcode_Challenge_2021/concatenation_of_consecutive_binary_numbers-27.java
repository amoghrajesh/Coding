class Solution {
    public int concatenatedBinary(int n) {
        long ans = 0;
        int size = 0;
        for(int i = 1; i <= n; i++){
            size = Integer.toBinaryString(i).length();
            ans = ((ans << size) + i) % 1000000007;
        }
        return (int)ans;
    }
}
