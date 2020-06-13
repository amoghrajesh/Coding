from collections import Counter
def stringAnagram(dictionary, query):
    hashmap = dict()
    ans = []
    for i in dictionary:
        x = ''.join(sorted(i))
        if x in hashmap:
            hashmap[x] += 1
        else:
            hashmap[x] = 1
    for q in query:
        x = ''.join(sorted(q))
        if x not in hashmap:
            ans.append(0)
        else:
            ans.append(hashmap[x])
    return ans
n = int(input())
dictionary =[]
for i in range(n):
    dictionary.append(input())


n = int(input())
query = []
for i in range(n):
    query.append(input())


stringAnagram(dictionary, query)