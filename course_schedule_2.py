from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        indeg = [0]*numCourses
        for i in prerequisites:
            u,v = i
            g[v].append(u)
            indeg[u] += 1

        q = []
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        top = []
        c = 0
        
        while q:
            u = q.pop(0)
            top.append(u)
            
            for i in g[u]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)
            c+=1
        
        if c == numCourses:
            return top
        return []