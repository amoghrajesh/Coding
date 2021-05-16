class Solution {
    int ans;
    Set<TreeNode> visited;
    public void dfs(TreeNode root, TreeNode parent){
        if(root != null){
            dfs(root.left, root);
            dfs(root.right, root);
            
            if(parent == null && visited.contains(root) == false || visited.contains(root.left) == false || visited.contains(root.right) == false){
                    visited.add(root);
                    visited.add(root.left);
                    visited.add(root.right);
                    visited.add(parent);
                    ans = ans + 1;
            }
        }   
    }
    
    public int minCameraCover(TreeNode root) {
        visited = new HashSet<>();
        visited.add(null);
        ans = 0;
        
        dfs(root, null);
        return ans;
    }
}
