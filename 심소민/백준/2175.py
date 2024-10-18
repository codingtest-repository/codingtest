'''
* Author    : SHIM SOMIN
* Date      : 2024.10.15(Tues)
* Runtime   : 68 ms
* Memory    : 34176 KB
* Algorithm : BFS
'''

from collections import deque

# 미로 탐색 함수
def bfs(maze, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0)])  # 시작점 (0, 0)
    maze[0][0] = 1

    while queue:
        x, y = queue.popleft()

        # 도착지점에 도달한 경우 경로의 길이 반환
        if x == n - 1 and y == m - 1:
            return maze[x][y]

        # 현재 위치에서 네 방향으로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 이동할 위치가 미로의 범위를 벗어나지 않고, 이동 가능한 칸(1)인 경우
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                # 이동할 칸의 경로 값을 현재 위치의 경로 값 + 1로 갱신
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

print(bfs(maze, n, m))
