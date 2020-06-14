n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1

cost = [10**9]*n
cost[src] = 0

adjCost = [[10**9]*n]*n
for f in edges:
    u, v, w = f[0], f[1], f[2]
    adjCost[u][v] = w

q = []
q.append(src)
stops = 0

while q:
    size = len(q)
    for i in range(size):
        c = q.pop(0)
        for f in edges:
            u, v = f[0], f[1]
            if stops == k and v != dst:
                continue
            if c == u and cost[v] > cost[u] + adjCost[u][v]:
                print("in", u, v)
                cost[v] = cost[u] + adjCost[u][v]
                q.append(v)
    stops+=1
print(cost)
print(cost[dst])
