def combinationSum3(k, n):
    results = []
    def backtrack(remain, comb, next_start):
        if remain == 0 and len(comb) == k:
            results.append(list(comb))
            return
        elif remain < 0 or len(comb) == k:
            return
        for i in range(next_start, 9):
            comb.append(i+1)
            backtrack(remain-i-1, comb, i+1)
            comb.pop()

    backtrack(n, [], 0)

    return results

n = 4
m = 4 
totalCost = 2
print(combinationSum3(n, totalCost))

