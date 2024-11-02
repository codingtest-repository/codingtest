'''
* Author    : Jang Woo Jin
* Date      : 2024.10.28(Mon)
* Runtime   : 52 ms
* Memory    : 34044 KB
* Algorithm : BFS
'''

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())

visited = [False] * (N+1)
cnt = 0

seq = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    seq[a].append(b)
    seq[b].append(a)

def BFS(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        v = q.popleft()
        for node in seq[v]:
            if not visited[node]:
                visited[node] = True
                q.append(node)

BFS(1)
for idx in range(len(visited)):
    if visited[idx]:
        cnt += 1
print(cnt - 1)