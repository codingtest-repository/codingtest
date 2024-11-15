'''
* Author    : BYEONGHO KANG
* Date      : 2024.11.15(Fri)
* Runtime   : 3772 ms
* Memory    : 34496 KB
* Algorithm : 백트래킹
'''
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
grid = [] 
boomList = deque()

R, C, N = map(int, input().split())

for i in range(R):
    row = list(input())
    for j in range(C):
        if row[j] == 'O':
            boomList.append([i, j])
    grid.append(row)

t = 1

while t < N:

    for i in range(R):
        for j in range(C):
            if grid[i][j] == '.':
                grid[i][j] = 'O'

    t += 1
    if t == N:
        break

    while boomList:
        x, y = boomList.popleft()
        grid[x][y] = '.'
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                grid[nx][ny] = '.'

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'O':
                boomList.append([i, j])

    t += 1

for g in grid:
    print(''.join(g))