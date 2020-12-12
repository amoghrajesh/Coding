class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
		# Find the deepest depth
        def find_depth(node, level):
            if not node: return level
            return max(find_depth(node.left, level + 1), find_depth(node.right, level + 1))
        
        def dfs(node, level, max_depth):
            if not node: return None
            if level == max_depth - 1: return node
            
            dl = dfs(node.left, level + 1, max_depth)
            dr = dfs(node.right, level + 1, max_depth)
            if dl and dr: return node
            return dl or dr
        
        max_depth = find_depth(root, 1)
        return dfs(root, 1, max_depth)