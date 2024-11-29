'''
* Author    : JUYEONG HA
* Date      : 2024.11.25(Mon)
* Runtime   : 96 ms
* Memory    : 31120 KB
* Algorithm : Dynamic Programming
'''

import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

dp = [0] * n # 연속하는 누적합

for i in range(n):
    hap = 0 # 이전 누적합 중 최대
    for prev_i in range(i):
        # prev_i가 i보다 작으면서, dp는 가장 큰 값을 찾음
        if lst[prev_i] < lst[i] and dp[prev_i] > hap:
            hap = dp[prev_i]

    dp[i] = hap + lst[i] # dp(누적합) 저장

print(max(dp))


