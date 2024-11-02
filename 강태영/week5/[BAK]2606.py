'''
* Author    : 강태영
* Date      : 2024.11.02(SAT)
* Runtime   : 
* Memory    : 
* Algorithm : BFS/DFS

https://www.acmicpc.net/problem/2606
바이러스(실버3)
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) #컴퓨터의 수
L = int(input()) #연결되어 있는 컴퓨터의 수

visited = [False]*(N+1)
graph = [[] for i in range(N+1)]

#graph 정보 담기
graph[0] = []
for n in range(1,L+1):
    a,b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

#print(visited)
#print(graph)
#bfs로 탐색
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)
#print(visited)
print(sum(visited)-1)