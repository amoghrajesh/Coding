from collections import defaultdict
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
def dfs(u):
    dest = graph[u]
    while dest:
        x = dest.pop(0)
        dfs(x)
    ans.append(u)

ans = []
graph = defaultdict(list)
tickets.sort(key = lambda x: x[1])
for u, v in tickets:
    graph[u].append(v)

dfs('JFK')
print(ans[::-1])
