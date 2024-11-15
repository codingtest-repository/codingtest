'''
* Author    : Jang Woo Jin
* Date      : 2024.11.15(Fri)
* Runtime   : 1968 ms
* Memory    : 34872 KB 
* Algorithm : Implementation, BFS
'''

import sys
input = sys.stdin.readline
from collections import deque

R, C, N = map(int, input().split())
bomb = deque()
board = []

# 지도 저장
for _ in range(R):
    board.append(list(input().strip()))

# 상하좌우 폭탄 폭발 구현
def BFS(bomb, board):
    while bomb:
        dy = [-1, 0, 1, 0]
        dx = [0, -1, 0, 1]
        y, x  = bomb.popleft()
        board[y][x] = '.'
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < R and 0 <= nx < C and board[ny][nx] == "O":
                board[ny][nx] = '.'

def setting(t):
    global bomb, board
    # 폭탄 위치 파악
    if t == 1:
        for i in range(R):
            for j in range(C):
                if board[i][j] == "O":
                    bomb.append([i, j])
    # 1초가 지난 후 3초 전에 설치된 폭탄이 모두 폭발한다.
    elif t % 2 == 1:
        BFS(bomb, board)
        for i in range(R):
            for j in range(C):
                if board[i][j] == "O":
                    bomb.append([i, j])
    else:
        board = [['O'] * C for _ in range(R)]

for i in range(1, N+1):
    setting(i)

for i in range(R):
    for j in range(C):
        print(board[i][j], end="")
    print()