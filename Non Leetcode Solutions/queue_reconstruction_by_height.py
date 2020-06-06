people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
people = sorted(people, key = lambda x: (-x[0], x[1]))
ans = []
for i in people:
    ans.insert(i[1], i)
print(ans)