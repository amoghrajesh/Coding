class Solution:
    def insert(self, intervals: List[List[int]], I: List[int]) -> List[List[int]]:
        bef = []
        aft = []
        
        for i in range(len(intervals)):
            x, y = intervals[i]
            if y < I[0]:
                bef.append([x, y])
            else:
                if I[1] < x:
                    aft.append([x, y])
                else:
                    I = [min(x, I[0]), max(y, I[1])]
        
        return bef + [I] + aft