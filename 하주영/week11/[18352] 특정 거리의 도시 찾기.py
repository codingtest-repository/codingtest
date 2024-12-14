'''
* Author    : JUYEONG HA
* Date      : 2024.12.13(Fri)
* Runtime   : 1348 ms 
* Memory    : 100912 KB
* Algorithm : BFS
'''


import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)



q = deque()
visited = [0] * (n+1)

q.append((x, 0))
visited[x] = -1

while q:
    v, cnt = q.popleft()

    for next_v in graph[v]:
        if not visited[next_v] and cnt < k: # 방문하지 않은 도시이면서, 최단 거리에 도달하지 않은 경우
            q.append((next_v, cnt +1))
            visited[next_v] = cnt + 1

flag = 0
for i in range(1, n+1):
    if visited[i] == k:
        print(i)
        flag = 1

if not flag:
    print(-1) 
