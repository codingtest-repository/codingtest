'''
* Author    : Jang Woo Jin
* Date      : 2024.09.29(Sun)
* Runtime   : 212 ms
* Memory    : 31120 KB
* Algorithm : floyd warshall
'''

import sys
input = sys.stdin.readline

N = int(input())
INF = float('inf')
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(len(lst)):
        if lst[j] == 1:
            graph[i+1][j+1] = 1

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            if graph[a][k] == 1 and graph[k][b] == 1:
                graph[a][b] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()