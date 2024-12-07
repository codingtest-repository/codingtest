'''
* Author    : JUYEONG HA
* Date      : 2024.12.06(Fri)
* Runtime   : 68 ms 
* Memory    : 34968 KB
* Algorithm : Simulation
'''

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
finish_list = list(map(int, input().split()))
start_list = [i for i in range(1, n+1)]

# max_k 구하기
max_k = 10
for i in range(max_k, 0, -1):
    if 2 ** i < n:
        max_k = i
        break

# 카드 섞기
def shake_cards(cards, cnt):
    q = deque(cards) # 카드 섞기 전 카드 리스트
    result_q = deque() # 카드 섞기 후 카드 리스트

    for i in range(cnt, -1, -1):
        power_two = 2 ** i
        cards_len = len(q)
        for _ in range(power_two): 
            q.appendleft(q.pop())
        for _ in range(cards_len-power_two):
            result_q.appendleft(q.pop())

    return list(q) + list(result_q)

# 1부터 max_k까지 2가지를 뽑는 조합
for i in range(1, max_k + 1):
    for j in range(1, max_k +1):
        temp_list = shake_cards(start_list, i)
        temp_list = shake_cards(temp_list, j)

        if temp_list == finish_list:
            print(i, j)
            break


