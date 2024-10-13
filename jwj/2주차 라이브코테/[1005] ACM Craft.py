# [문제 출처] : https://www.acmicpc.net/problem/1005

import sys
input = sys.stdin.readline
from collections import deque

def topology_sort():
    for i in range(1, len(indegree)):
        if indegree[i] == 0:    # 제약 조건이 없는 것들 먼저 처리
            q.append(i)
            tt[i] = st[i]

    while q:
        v = q.popleft()
        for i in sequence[v]:
            indegree[i] -= 1
            tt[i] = max(tt[i], st[i] + tt[v])
            if indegree[i] == 0:
                q.append(i)

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    st = [0] + list(map(int, input().split()))      # zero base
    sequence = [[] for _ in range(N+1)]             # zero base
    indegree = [0] * (N+1)                          # zero base
    tt = [0] * (N+1)                                # zero base

    for _ in range(K):
        a, b = map(int, input().split())    
        sequence[a].append(b)
        indegree[b] += 1                # b작업을 하기 위해서 a작업을 해야한다는 것이 선결조건
        
    q = deque()
    topology_sort()
    W = int(input())
    print(tt[W])