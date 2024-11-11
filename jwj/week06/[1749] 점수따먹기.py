'''
* Author    : Jang Woo Jin
* Date      : 2024.11.08(Fri)
* Runtime   : 3744 ms
* Memory    : 111028 KB (PyPy3)
* Algorithm : Dynamic Programming
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
INF = -int(1e8)

for i in range(1, N+1):
    for j in range(1, M+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + board[i-1][j-1]

ans = INF
for y1 in range(1, N+1):
    for x1 in range(1, M+1):
        for y2 in range(y1, N+1):
            for x2 in range(x1, M+1):
                ans = max(ans, prefix_sum[y2][x2] - prefix_sum[y2][x1 - 1] - prefix_sum[y1 - 1][x2] + prefix_sum[y1 - 1][x1 - 1])
print(ans)