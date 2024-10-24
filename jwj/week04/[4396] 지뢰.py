'''
* Author    : Jang Woo Jin
* Date      : 2024.10.24(Thu)
* Runtime   : 32 ms
* Memory    : 31120 KB
* Algorithm : implementation
'''

import sys
input = sys.stdin.readline

# 상하좌우 대각선 전부 포함
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

N = int(input())
mine = [list(map(str, input().strip())) for _ in range(N)]
play = [list(map(str, input().strip())) for _ in range(N)]
result = [['.'] * N for _ in range(N)]

mine_pos = []
for i in range(len(mine)):
    for j in range(len(mine[i])):
        if mine[i][j] == "*":
            mine_pos.append([i, j])

for i in range(len(play)):
    for j in range(len(play[i])):
        
        # 지뢰가 없는 지점이면서 이미 열린 칸인 경우라면 숫자가 나타나야 한다.
        if play[i][j] == "x" and mine[i][j] == ".":
            cnt = 0
            for t in range(8):
                ny = i + dy[t]
                nx = j + dx[t]
                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue
                if [ny, nx] in mine_pos:
                    cnt += 1
            result[i][j] = cnt

        # 지뢰가 있는 칸을 열었다면 
        if play[i][j] == "x" and mine[i][j] == "*":
            for y in range(N):
                for x in range(N):
                    if mine[y][x] == "*":
                        result[y][x] = "*"

for i in range(N):
    for j in range(N):
        print(result[i][j], end="")
    print()