candies = [4,2,1,1,2]
extraCandies = 1
m = max(candies)

ans = []
for i in candies:
    if i+extraCandies>=m:
        ans.append(True)
    else:
        ans.append(False)
print(ans)
