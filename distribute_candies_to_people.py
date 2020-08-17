candies = 10
num_people = 3
ans = [0]*num_people
i = 0
cur = 1
n = num_people
while 1:
    if candies - cur <= 0:
        ans[i] += candies
        print(ans)
        break
    ans[i] += cur
    candies -= cur
    cur += 1
    i = (i + 1)%n