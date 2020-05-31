n = int(input())
c = list(map(int, input().split()))
min_dists = []
for city in range(n):

    m = 10**9
    for st in c:
        d = abs(city -  st)
        if d<m:
            m = d

    min_dists.append(m)



print(max(min_dists))


