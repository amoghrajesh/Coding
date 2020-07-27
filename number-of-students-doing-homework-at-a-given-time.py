class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        z = list(zip(startTime, endTime))
        ans = 0
        for i in z:
            s, e = i
            if queryTime >= s and queryTime <= e:
                ans += 1
        return ans