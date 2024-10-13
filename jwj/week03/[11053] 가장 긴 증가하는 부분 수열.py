'''
* Author    : Jang Woo Jin
* Date      : 2024.10.13(Sun)
* Runtime   : 144 ms
* Memory    : 31120 KB
* Algorithm : dynamic programming
'''

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [1] * N

for a in range(N):
    for b in range(a):
        if A[a] > A[b]:
            dp[a] = max(dp[a], dp[b] + 1)
print(max(dp))