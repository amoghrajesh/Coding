n, c = list(map(int, input().split()))
candies = list(map(int, input().split()))
m = int(input())
friends = []

hashmap = dict()
for i in range(m):
    x, y = list(map(int, input().split()))
    friends.append([x, y])
    if x in hashmap:
        hashmap[x].append(y)
    else:
        hashmap[x] = []
    
flag = [1]*n
for x, y in friends:
    if candies[x-1] + candies[y-1] >= c:
        flag[x-1] = flag[y-1] = 0
print(flag) 

ans = 0
for i in range(len(flag)):
    x = i
    if flag[x]:
        if x in hashmap:
            g = candies[x]
            for y in hashmap[y]:
                g += candies[y]
            if g <= c:
                c -= g
                ans += (1 + len(hashmap[x]))
            else:
                flag[x] = 0
                for y in hashmap[x]:
                    flag[y] = 0
        else:
            if candies[x] <= c:
                c -= candies[x]
                ans += 1
return ans

# 4 40
# 10 20 30 40
# 1
# 2 3





