class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [n-1]
        
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        hashmap = dict()
        
        for root in range(0, n):
            q = []
            q.append(root)
            dp = [0] * n
            visited = [False] * n
            visited[root] = True
            
            while q:
                temp = q.pop(0)
                for neigh in graph[temp]:
                    if not visited[neigh]:
                        q.append(neigh)
                        visited[neigh] = True
                    
                for i in q:
                    if not dp[i]:
                        dp[i] = dp[temp] + 1            
            
            h = max(dp)
            hashmap[root] = h
        print(hashmap)
        mht = min(hashmap.values())
        ans = []
        for i in hashmap:
            if hashmap[i] == mht:
                ans.append(i)
        return ans