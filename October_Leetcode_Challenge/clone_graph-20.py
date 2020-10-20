class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        def dfs(node):
            if not node:
                return None
            graph[node] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor not in graph:
                    dfs(neighbor)
                graph[node].neighbors += [graph[neighbor]]
        
        if not node:
            return None
        graph = dict()
        dfs(node)
        return graph[node]