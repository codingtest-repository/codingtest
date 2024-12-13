'''
* Author    : BYEONGHO KANG
* Date      : 2024.12.13(Fri)
* Runtime   : 232 ms
* Memory    : 32412 KB
* Algorithm : 그래프
'''

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for row in graph:
    print(*row)
