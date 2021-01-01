class Solution {
    public int maximum(int nums[], int l, int r){
        int m = l;
        for(int i = l; i < r; i++){
            if(nums[i] > nums[m]){
                m = i;
            }
        }
        return m;
    }
    public TreeNode helper(int nums[], int l, int r){
        if(l >= r){
            return null;
        }
        int m = maximum(nums, l, r);
        TreeNode root = new TreeNode(nums[m]);
        root.left = helper(nums, l, m);
        root.right = helper(nums, m + 1, r);
        
        return root;
    }
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return helper(nums, 0, nums.length);
    }
}