'''
* Author    : Jang Woo Jin
* Date      : 2024.10.12(Sat)
* Runtime   : 72 ms
* Memory    : 34060 KB
* Algorithm : BFS
'''


import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def BFS(a, b):
    q = deque()
    q.append([a, b])
    visited[a][b] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                if maps[ny][nx] == 1:
                    maps[ny][nx] = maps[y][x] + 1
                    visited[ny][nx] = True
                    q.append([ny, nx])

BFS(0, 0)
print(maps[N-1][M-1])