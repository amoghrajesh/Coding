paths = [["A","Z"]]
cities = set()
first = set()
for i in paths:
    cities.add(i[0])
    cities.add(i[1])
    first.add(i[0])

print(list(cities.difference(first))[0])
