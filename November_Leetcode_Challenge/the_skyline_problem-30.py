from collections import defaultdict
from heapq import *
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        res = []
        
        visited_building = [True] + [False] * len(buildings)
        
        hashmap = defaultdict(list)
        for i in range(len(buildings)):
            s, e, h = buildings[i]
            hashmap[s].append(i + 1)
            hashmap[e].append(-1 * (1 + i))
        
        
        build_heap = [(0, 0)]
        prev = 0
        
        heapify(build_heap)
        
        for x in sorted(hashmap.keys()):
            for i in hashmap[x]:
                # start
                if i > 0:
                    visited_building[i] = True
                    heappush(build_heap, (-1 * buildings[i - 1][2], i))
                else:
                    visited_building[-1 * i] = False
            while not visited_building[build_heap[0][1]]:
                heappop(build_heap)
            
            # if we visit a new building, do this
            if prev + build_heap[0][0]:
                res.append([x, -1 * build_heap[0][0]])
                prev = -1 * build_heap[0][0]
        
        return res