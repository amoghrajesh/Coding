class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], k: int) -> int:
        if not timeSeries:
            return 0
        arr = []
        for i in timeSeries:
            arr.append([i, i + k - 1])
        
        arr.sort(key = lambda x: x[0])
        index = 0
        for i in range(1, len(timeSeries)):
            if arr[index][1] >= arr[i][0]:
                arr[index] = [min(arr[index][0], arr[i][0]), max(arr[index][1], arr[i][1])]
            else:
                index += 1
                arr[index] = arr[i]
        ans = 0
        for j in range(index + 1):
            i = arr[j]
            ans += (i[1] - i[0] + 1)
        return ans