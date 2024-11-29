'''
* Author    : JUYEONG HA
* Date      : 2024.11.26(Tue)
* Runtime   : 48 ms
* Memory    : 31120 KB
* Algorithm : Dynamic Programming
'''

import sys

input = sys.stdin.readline

total_customers, count_of_cities = map(int, input().split())


data = []
for _ in range(count_of_cities):
    cost, customers = map(int,input().split())
    data.append((cost, customers))

dp = [1e7] * (total_customers + 101) # 여유롭게 101을 더 받음
dp[0] = 0 # 0명을 대상으로 하는 비용은 0

for cost, customers in data: # 각 도시에 대해 반복
    for i in range(1, total_customers + 101):
        if i >= customers: # 현재 고객 수가 더 많으면 갱신
            dp[i] = min(dp[i-customers] + cost, dp[i]) # 이전 누적합 + 현재 비용 vs 현재 누적합

print(min(dp[total_customers:])) # 최소 비용 출력

# 스스로 풀지 못함

