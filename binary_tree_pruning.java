class Solution {
    public boolean subtreeHasOne(TreeNode root){
        if(root == null){
            return false;
        }
        boolean leftTree = subtreeHasOne(root.left);
        if(leftTree == false){
            root.left = null;
        }
        boolean rightTree = subtreeHasOne(root.right);
        if(rightTree == false){
            root.right = null;
        }
        
        return root.val == 1 || leftTree || rightTree;
    }

    
    public TreeNode pruneTree(TreeNode root) {
        boolean ans = subtreeHasOne(root);
        return ans != true ? null : root;
    }
}
