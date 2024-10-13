# [문제 출처] : https://www.acmicpc.net/problem/3109

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dy = [-1, 0, 1]

R, C = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
result = 0

def recursive(y, x):
    if x == C - 1:
        return True
    
    for i in range(3):
        ny = y + dy[i]
        
        if 0 <= ny < R and board[ny][x+1] != "x" and not visited[ny][x+1]:
            visited[ny][x+1] = True
            if recursive(ny, x+1):
                return True
    return False

for i in range(R):
    visited[i][0] = True
    flag = recursive(i, 0)
    if flag:
        result += 1
print(result)