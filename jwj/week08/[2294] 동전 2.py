'''
* Author    : Jang Woo Jin
* Date      : 2024.11.22(Fri)
* Runtime   : 348 ms
* Memory    : 31120 KB 
* Algorithm : Dynamic Programming
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
vs = []
for _ in range(n):
    vs.append(int(input()))

dp = [10001] * (k+1)
dp[0] = 0
for v in vs:
    for i in range(v, len(dp)):
        dp[i] = min(dp[i], dp[i - v] + 1)

if dp[k] == 10001:
    print(-1)
    sys.exit(0)
print(dp[k])