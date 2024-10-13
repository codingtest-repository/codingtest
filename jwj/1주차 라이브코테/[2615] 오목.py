# [문제 출처] : https://www.acmicpc.net/problem/2615

import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

# ↗  →  ↘  ↓  
dy = [-1, 0, 1, 1]
dx = [1, 1, 1, 0]

for y in range(19):
    for x in range(19):
        if board[y][x] != 0:
            first = board[y][x]
            
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                cnt = 1
                
                while 0 <= ny < 19 and 0 <= nx < 19 and board[ny][nx] == first:
                    cnt += 1
                    
                    if cnt == 5:
                        if 0 <= y - dy[i] < 19 and 0 <= x - dx[i] < 19 and first == board[y - dy[i]][x - dx[i]]:
                            break
                        if 0 <= ny + dy[i] < 19 and 0 <= nx + dx[i] < 19 and first == board[ny + dy[i]][nx + dx[i]]:
                            break
                        
                        print(first)
                        print(y+1, x+1)
                        sys.exit(0)
                    else:
                        ny += dy[i]
                        nx += dx[i]
print(0)