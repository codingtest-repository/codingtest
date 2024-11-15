'''
* Author    : Jang Woo Jin
* Date      : 2024.11.15(Fri)
* Runtime   : 116 ms
* Memory    : 37696 KB 
* Algorithm : Prefix Sum
'''

import sys
input = sys.stdin.readline

N, K, Q, M = map(int, input().split())
k_lst = list(map(int, input().split()))
q_lst = list(map(int, input().split()))

panel = []
for _ in range(M):
    S, E = map(int, input().split())
    panel.append([S, E])

sleep = [0] * (N + 3)   # 자는지 여부 체크
check = [0] * (N + 3)   # 출석 체크

for k in k_lst:
    sleep[k] = 1

for q in q_lst:
    if sleep[q]:
        continue
    for nq in range(q, N+3, q):
        if not sleep[nq]:
            check[nq] = 1

prefix_sum = [0] * (N+3)

# prefix_sum : 결국 출석한 학생들의 누적 합 배열
for i in range(3, N+3):
    prefix_sum[i] = check[i] + prefix_sum[i-1]

for a, b in panel:
    print((b - a + 1) - (prefix_sum[b] - prefix_sum[a-1]))