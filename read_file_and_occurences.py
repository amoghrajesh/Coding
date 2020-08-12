text = open("sample.txt", "r")
hashmap = dict()
for line in text:
    words = line.split()
    for j in words:
        if j in hashmap:
            hashmap[j] += 1
        else:
            hashmap[j] = 1
print(hashmap)