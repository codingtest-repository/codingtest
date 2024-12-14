'''
* Author    : JUYEONG HA
* Date      : 2024.12.04(Wed)
* Runtime   : 36 ms
* Memory    : 31120 KB
* Algorithm : Dynamic Programming
'''

import sys

input = sys.stdin.readline

N = int(input())
returns = [0] * (N + 1)

for i in range(1, N+1):
    elapsed_time, profit = map(int, input().split())

    max_profit = max(returns[:i]) # 지금까지 벌어드린 수익 중 최대
    finish_counsel = i + elapsed_time - 1 # 상담 끝나는 일
    

    if finish_counsel <= N: # 범위(퇴사일)를 넘어가지 않는 조건
        returns[finish_counsel] = max(max_profit + profit, returns[finish_counsel]) # i일까지 받을 수 있는 일에서의 최대 수익   

print(max(returns))
