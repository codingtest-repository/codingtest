'''
* Author    : BYEONGHO KANG
* Date      : 2024.11.1(Fri)
* Runtime   : 308 ms
* Memory    : 34072 KB
* Algorithm : Graph, BFS, DFS
'''
from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for node in sorted(graph[start]):
        if not visited[node]:
            dfs(graph, node, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for node in sorted(graph[current]):
            if not visited[node]:
                visited[node] = True
                queue.append(node)

N, M, V = map(int, input().split())
# Python Dictionary 자료형 사용
graph = {}
for i in range(1, N + 1):
    graph[i] = []
    
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
dfs(graph, V, visited)
print()

visited = [False] * (N + 1)
bfs(graph, V, visited)
print()