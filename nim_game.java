class Solution {
    public boolean canWinNim(int n) {
        // I am in losing position
        boolean ans = (n % 4 == 0);
        return !ans;
    }
}