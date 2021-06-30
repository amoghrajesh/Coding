class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null){
            return null;
        }
        
        if(root == p || root == q){
            return root;
        }
        
        TreeNode leftSubtree = lowestCommonAncestor(root.left, p, q);
        TreeNode rightSubtree = lowestCommonAncestor(root.right, p, q);
        
        boolean nodeFound = leftSubtree != null && rightSubtree != null;
        if(nodeFound){
            return root;
        }
        
        return leftSubtree == null ? rightSubtree : leftSubtree;
        
    }
}
