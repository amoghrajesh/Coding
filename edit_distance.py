

def editDist(word1, word2, m ,n):
    if m==0:
        return n
    if n == 0:
        return m

    if word1[m-1] == word2[n-1]:
        return editDist(word1, word2, m-1, n-1)

    return 1 + min(editDist(word1, word2, m, n-1), editDist(word1, word2, m-1, n-1), editDist(word1, word2, m-1, n))



word1 = input()
word2 = input()
print(editDist(word1,word2,len(word1),len(word2)))
# m = len(word1)
# n = len(word2)
# dp = []
# for i in range(m+1):
#     dp.append([0]*(n+1))
#
# for i in range(m+1):
#     for j in range(n+1):
#         if i==0:
#             dp[i][j] = j
#         if j ==0:
#             dp[i][j] = i
#
#         if word1[i-1] == word2[j-1]:
#             dp[i][j] = dp[i-1][j-1]
#
#         else:
#             dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
#
# print(dp[-1][-1])







