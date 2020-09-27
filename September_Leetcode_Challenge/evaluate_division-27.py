from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        hashmap = defaultdict(dict)
        n = len(equations)
        
        for i in range(n):
            p = equations[i][0]
            q = equations[i][1]
            k = values[i]
            # p/q = k
            hashmap[p][q] = k
            hashmap[p][p] = 1.0
            hashmap[q][p] = 1/k
            hashmap[q][q] = 1.0
        print(hashmap)
        
        
    

        def dfs(hashmap, node, dest, val, visited):
            nodemap = hashmap[node]
            if dest in nodemap:
                return val * nodemap[dest]
            
            visited.add(node)
            for u, w in nodemap.items():
                if u not in visited:
                    val2 = dfs(hashmap, u, dest, val * w, visited)
                    if val2 >= 0: return val2
            return -1
                
        


        ans = []
        for i in queries:
            p = i[0]
            q = i[1]
            
            if p not in hashmap or q not in hashmap:
                ans.append(-1.0)
            elif p == q:
                ans.append(1.0)
            elif q in hashmap[p]:
                ans.append(hashmap[p][q])
            else:
                f = 1
                visited = set()
                src, dest = p, q
                ans.append(dfs(hashmap, src, dest, 1.0, visited))
        return ans
                        