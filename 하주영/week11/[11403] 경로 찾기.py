'''
* Author    : JUYEONG HA
* Date      : 2024.12.14(Sat)
* Runtime   : 92 ms 
* Memory    : 34924 KB
* Algorithm : BFS
'''

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
adj_lst = [list(map(int, input().split())) for _ in range(n)]
answer_lst = [[0] * n for _ in range(n)]

def bfs(v):
    global n, answer_lst
    
    q = deque()
    visited = set()

    q.append(v)

    while q:
        cur_v = q.popleft()

        for next_v in range(n):
            if next_v not in visited and adj_lst[cur_v][next_v] == 1:
                q.append(next_v)
                visited.add(next_v)
    
    for i in range(n):
        if i in visited:
            answer_lst[v][i] = 1

for i in range(n):
    bfs(i)

for row in answer_lst:
    print(*row)
    
