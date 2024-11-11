'''
* Author    : Jang Woo Jin
* Date      : 2024.11.08(Fri)
* Runtime   : 116 ms
* Memory    : 41688 KB
* Algorithm : Dynamic Programming
'''

import sys
input = sys.stdin.readline

N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = triangle[0][0]

for i in range(1, N):
    dp[i][0] += dp[i-1][0] + triangle[i][0]
    dp[i][i] += dp[i-1][i-1] + triangle[i][i]

for i in range(2, N):
    for j in range(1, i):
        dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])

result = 0
for i in range(N):
    MAX = max(dp[i])
    result = max(result, MAX)
print(result)