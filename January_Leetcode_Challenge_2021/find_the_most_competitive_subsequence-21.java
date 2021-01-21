class Solution {
    public int[] mostCompetitive(int[] nums, int k) {
        if(nums.length == k){
            return nums;
        }
        int n = nums.length;
        int remaining = n;
        Stack<Integer> s = new Stack<>();
        for(int i = 0; i < n; i++){
            remaining = n - i - 1;
            while(s.empty() == false && s.size() + remaining >= k && s.peek() > nums[i]){
                s.pop();
            }
            s.push(nums[i]);
        }
        Stack<Integer> rev = new Stack<>();
        while(s.empty() == false){
            rev.push(s.pop());
        }
        int[] ans = new int[k];
        int j = 0;
        while(j < k && rev.empty() == false){
            ans[j++] = rev.peek();
            rev.pop();
        }
        return ans;
    }
}
