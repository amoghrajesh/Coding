class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        max_till_now = -10**9
        merged = 0
        
        for i in range(len(intervals)):
            if intervals[i][1] <= max_till_now:
                merged += 1
            else:
                max_till_now = intervals[i][1]
        return len(intervals) - merged