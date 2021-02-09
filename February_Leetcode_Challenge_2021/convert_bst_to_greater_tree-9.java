class Solution {
    List<Integer> l = new ArrayList<>();
    HashMap<Integer, Integer> map = new HashMap<>();
    
    public void inorder(TreeNode root){
        if(root == null){
            return;
        }
        inorder(root.left);
        l.add(root.val);
        inorder(root.right);
    }
    
    public void changeTree(TreeNode root){
        if(root == null){
            return;
        }
        root.val = map.get(root.val);
        changeTree(root.left);
        changeTree(root.right);
    }
    
    public TreeNode convertBST(TreeNode root) {
        if(root == null){
            return root;
        }
        inorder(root);
        
        int n = l.size();
        map.put(l.get(n - 1), l.get(n - 1));
        for(int i = n - 2; i > -1; i--){
            map.put(l.get(i), l.get(i) + map.get(l.get(i + 1)));
        }
        
        changeTree(root);
        return root;
    }
}
