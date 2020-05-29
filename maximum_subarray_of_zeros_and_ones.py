l= list(map(int,input().split()))
hashmap = dict()
hashmap[0] = -1
cur_sum = 0
max_len = 0
for i in range(len(l)):
    if l[i] == 0:
        cur_sum -= 1
    else:
        cur_sum += 1

    if cur_sum in hashmap:
        max_len = i - hashmap[cur_sum]
    else:
        hashmap[cur_sum] = i

print(max_len)