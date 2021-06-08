class Solution {
    int pre = 0;
    Map<Integer, Integer> map = new HashMap<>();
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for(int i = 0; i < inorder.length; i++){
            map.put(inorder[i], i);
        }
        
        TreeNode tree = buildTree(preorder, 0, inorder.length - 1);
        return tree;
    }
    
    public TreeNode buildTree(int[] preorder, int left, int right){
        if(left > right){
            return null;
        }
        int nodeValue = preorder[pre++];
        TreeNode root = new TreeNode(nodeValue);
        
        root.left = buildTree(preorder, left, map.get(nodeValue) - 1);
        root.right = buildTree(preorder, map.get(nodeValue) + 1, right);
        
        return root;
    }
}
