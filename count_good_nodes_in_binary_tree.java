class Solution {
    int count = 0;
    
    public void preorder(TreeNode root, int max){
        if(root == null){
            return;
        }    
        
        if(root.val >= max){
            max = root.val;
            count++;
        }
        
        preorder(root.left, max);
        preorder(root.right, max);
    }
    
    public int goodNodes(TreeNode root) {
        preorder(root, Integer.MIN_VALUE);
        return count;
    }
}