'''
* Author    : Jang Woo Jin
* Date      : 2024.10.22(Tue)
* Runtime   : 652 ms
* Memory    : 50492 KB
* Algorithm : topology sort
'''


import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
seq = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
result = [1] * (N+1)

def topology_sort():
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        v = q.popleft()
        for i in seq[v]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                result[i] = result[v] + 1

for _ in range(M):
    a, b = list(map(int, input().split()))
    seq[a].append(b)
    indegree[b] += 1

topology_sort()
print(*result[1:])