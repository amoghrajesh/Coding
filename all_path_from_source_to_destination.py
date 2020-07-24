from collections import defaultdict
class Solution(object):
    def allPathsSourceTarget(self, graph):
        g = defaultdict(list)
        for i in range(len(graph)):
            edges = graph[i]
            for edge in edges:
                g[i].append(edge)
        s = 0
        d = len(graph) - 1
        def dfs(u, d, g, visited, path):
            visited[u] = True
            path.append(u)
            if u == d:
                ans.append(path[::])
            else:
                for i in g[u]:
                    if visited[i] == False:
                        dfs(i, d, g, visited, path)
            
            path.pop()
            visited[u] = False
        ans = []
        dfs(s, d, g, [False]*len(graph), [])
        return ans