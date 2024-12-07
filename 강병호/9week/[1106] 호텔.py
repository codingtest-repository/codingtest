'''
* Author    : BYEONGHO KANG
* Date      : 2024.11.29(Fri)
* Runtime   : 40 ms
* Memory    : 31120 KB
* Algorithm : 다이나믹 프로그래밍
'''

C, N = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(N)]

dp = [float('inf')] * (C + 101)
dp[0] = 0

for cost, customers in cities:
    for i in range(customers, C + 101):
        dp[i] = min(dp[i], dp[i - customers] + cost)

print(min(dp[C:]))
