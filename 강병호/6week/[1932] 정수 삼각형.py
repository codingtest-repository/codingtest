'''
* Author    : BYEONGHO KANG
* Date      : 2024.11.8(Fri)
* Runtime   : 120 ms
* Memory    : 40264 KB
* Algorithm : 다이나믹 프로그래밍
'''


import sys
input = sys.stdin.read

data = input().splitlines()
n = int(data[0])
triangle = [list(map(int, line.split())) for line in data[1:n+1]]

dp = [[0] * (i + 1) for i in range(n)]
dp[0][0] = triangle[0][0] 

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            # left
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
        elif j == i:
            # right
            dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        else:
            # middle
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

print(max(dp[n - 1]))
