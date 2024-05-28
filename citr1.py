import heapq
def maxPerformance(n, speed, reliablity, maxMachines):
    
    people = sorted(zip(speed, reliablity), key=lambda x: -x[1])
    result, sum_speed = 0, 0
    min_heap = []
    
    for i, (s, e) in enumerate(people):
        if i < maxMachines:
            sum_speed += s
            heapq.heappush(min_heap, s)
        elif s > min_heap[0]:
            sum_speed += s - heapq.heappushpop(min_heap, s)
        
        result = max(result, sum_speed * e)
    
    return result # % 1000000007


n = 5
speed = [4,3,15,5,6]
reliablity = [7,6,1,2,8]
maxMachines = 3
print(maxPerformance(n, speed, reliablity, maxMachines))
