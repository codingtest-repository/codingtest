'''
* Author    : Jang Woo Jin
* Date      : 2024.10.20(Sun)
* Runtime   : 76 ms
* Memory    : 34096 KB
* Algorithm : topology sort
'''

import sys
input = sys.stdin.readline
from collections import deque

def topology_sort():
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            result[i] = st[i]
    
    while q:
        v = q.popleft()
        for i in seq[v]:
            indegree[i] -= 1
            result[i] = max(result[i], result[v] + st[i])
            if indegree[i] == 0:
                q.append(i)

N = int(input())

seq = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
st = [0] * (N+1)
result = [0] * (N+1)

for num in range(1, N+1):
    data = list(map(int, input().split()))[:-1]
    st[num] = data[0]

    data = data[1:]
    for i in data:
        seq[i].append(num)
        indegree[num] += 1

topology_sort()

for i in range(1, len(result)):
    print(result[i])