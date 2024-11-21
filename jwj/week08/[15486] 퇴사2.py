'''
* Author    : Jang Woo Jin
* Date      : 2024.11.21(Thr)
* Runtime   : 2540 ms
* Memory    : 168760 KB 
* Algorithm : Dynamic Programming
'''

import sys
input = sys.stdin.readline

N = int(input())

T = [0 for i in range(N+1)]
P = [0 for i in range(N+1)]
dp = [0 for i in range(N+1)]

for i in range(1, N+1):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i-1])
    deadline = i + T[i] - 1
    if deadline <= N:
        dp[deadline] = max(dp[deadline], dp[i - 1] + P[i])
print(max(dp))

    