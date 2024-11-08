'''
* Author    : Jang Woo Jin
* Date      : 2024.11.08(Fri)
* Runtime   : 3472 ms
* Memory    : 117032 KB (PyPy3)
* Algorithm : Implementation
'''

import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

answer = 0
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().strip().split())
    for a in range(i-1, x):
        for b in range(j-1, y):
            answer += arr[a][b]
    print(answer)
    answer = 0