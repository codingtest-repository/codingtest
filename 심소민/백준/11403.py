"""
* Author    : SHIM SOMIN
* Date      : 2024.10.01 (Tue)
* Runtime   : 156 ms 
* Memory    : 31120 KB  
* Algorithm : 그래프
 """

N = int(input())  # 정점의 개수
graph = [list(map(int, input().split())) for _ in range(N)]

# 플로이드-워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            # i에서 j로 가는 경로가 있거나, i -> k -> j 경로가 있을 때
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

# 결과 출력
for row in graph:
    print(" ".join(map(str, row)))
