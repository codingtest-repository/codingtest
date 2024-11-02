'''
선수과목
https://www.acmicpc.net/problem/14567
'''
import sys
from collections import deque
input = sys.stdin.readline

#과목 수: N, 선수 조건의 수: M
N, M = map(int, (input().split()))
#진입 차수
indegree = [0]*(N+1)
#깊이 넣기
depth = [0]*(N+1)
#노드에 연결된 간선 정보를 담기 위한 연결리스트
graph = [[] for i in range(N+1)]

#방향 그래프의 모든 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort(): #위상정렬
    q = deque()

    #차원이 0인 것 넣기
    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)
            depth[i] = 1

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                depth[i] = depth[now] + 1

    return depth

result = topology_sort()
print(' '.join(map(str, result[1:])))