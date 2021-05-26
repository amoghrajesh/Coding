class Solution {
    public int minPartitions(String n) {
        int ans = 0;
        for(int i = 0; i < n.length(); i++){
            char c = n.charAt(i);
            int digit = Character.getNumericValue(c);
            ans = Math.max(ans, digit);
        }
        return ans;
    }
}
