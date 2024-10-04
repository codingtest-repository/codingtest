'''
* Author    : Yooyoung Lee
* Date      : 2024.10.02(Wed)
* Runtime   : 152 ms
* Memory    : 31120 KB
* Algorithm : F-W
'''
import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# F-W
for k in range(n):
    for a in range(n):
        for b in range(n):
            matrix[a][b] = matrix[a][b] or (matrix[a][k] and matrix[k][b])

# print result
for row in range(n):
    print(*matrix[row])
