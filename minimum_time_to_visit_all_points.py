points = [[3,2],[-2,2]]
n = len(points)
time = 0
for i in range(n-1):
    time += max(abs(points[i][0] - points[i + 1][0]), abs(points[i][1] - points[i + 1][1])) 

print(time)