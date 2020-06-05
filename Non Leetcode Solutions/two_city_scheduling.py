costs = [[10,20],[30,200],[400,50],[30,20]]
n = len(costs)
a = 0
b = 0
#the ones earlier are better sent to A
diff_of_distance = sorted(costs, key = lambda x: x[0] - x[1])
for i in range(n//2):
    a += diff_of_distance[i][0]
for i in range(n//2,n):
    b += diff_of_distance[i][1]
print(a + b)
