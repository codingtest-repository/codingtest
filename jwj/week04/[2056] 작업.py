import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
seq = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
dp = [0] * (N+1)
st = [0] * (N+1)

def topology_sort():
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = st[i]

    while q:
        v = q.popleft()
        for i in seq[v]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[v] + st[i])
            if indegree[i] == 0:
                q.append(i)

for i in range(1, N+1):
    data = list(map(int, input().split()))
    st[i] = data[0]
    cnt = data[1]
    if cnt == 0:
        continue
    else:
        lst = data[2:]
        for j in lst:
            seq[j].append(i)
            indegree[i] += 1

topology_sort()
print(max(dp))