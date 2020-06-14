n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
K = 1
K+=1

cost = [10**9]*n
cost[src] = 0
for trip_len in range(K):
    for u, v, w in flights:
        cost[v] = min(cost[u] + w, cost[v])
print(cost[dst] if cost[dst]!=10**9 else -1)
