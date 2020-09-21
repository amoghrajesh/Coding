class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips:
            return True
        m = max(trips, key = lambda x : x[2])
        m = m[-1]
        
        l = [0] * (m + 1)
        
        for i in range(len(trips)):
            cap = trips[i][0]
            start = trips[i][1]
            end = trips[i][2]
            for j in range(start, end):
                l[j] += cap
                if l[j] > capacity:
                    return False
        return True