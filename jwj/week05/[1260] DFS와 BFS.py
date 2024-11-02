'''
* Author    : Jang Woo Jin
* Date      : 2024.10.28(Mon)
* Runtime   : 108 ms
* Memory    : 34096 KB
* Algorithm : DFS & BFS
'''

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)
seq = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    seq[a].append(b)
    seq[b].append(a)
    seq[a].sort()
    seq[b].sort()
    
def DFS(start):
    dfs_visited[start] = True
    print(start, end=" ")
    for i in range(1, N+1):
        if not dfs_visited[i] and i in seq[start]:
            DFS(i)

def BFS(start):
    q = deque()
    q.append(start)
    bfs_visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for idx in seq[v]:
            if not bfs_visited[idx] and idx in seq[v]:
                bfs_visited[idx] = True
                q.append(idx)

DFS(V)
print()
BFS(V)