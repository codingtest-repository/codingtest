'''
* Author    : Yooyoung Lee
* Date      : 2024.10.15(Tues)
* Runtime   : 76 ms
* Memory    : 34060 KB
* Algorithm : BFS
'''
import sys

input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
MAP = [input() for _ in range(n)]

visited = [[False] * m for _ in range(n)]

queue = deque([(0, 0, 1)])  # x, y, 칸수
visited[0][0] = True
while queue:
    cx, cy, cnt = queue.popleft()
    if (cx, cy) == (m - 1, n - 1):
        print(cnt)
        break
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= dy + cy < n and 0 <= dx + cx < m and MAP[dy + cy][dx + cx] == '1' and not visited[dy + cy][dx + cx]:
            queue.append((dx + cx, dy + cy, cnt + 1))
            visited[dy + cy][dx + cx] = True