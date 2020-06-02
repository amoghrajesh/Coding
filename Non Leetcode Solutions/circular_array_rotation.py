n,k,q = list(map(int,input().split()))
l = list(map(int,input().split()))

# we can only have n%k varieties

hashmap = dict()
hashmap[0] = l

# if k is huge, we should know that we can have only n varieties of it
for i in range(1, n):
    hashmap[i] = [hashmap[i - 1][-1]] + hashmap[i - 1][:len(hashmap[i - 1]) - 1]
k = k % n
ans = hashmap[k]

for i in range(q):
    print(ans[int(input())])




