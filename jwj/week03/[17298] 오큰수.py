'''
* Author    : Jang Woo Jin
* Date      : 2024.10.13(Sun)
* Runtime   : 1440 ms
* Memory    : 220564 KB
* Algorithm : data structure
'''

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
nge = [-1] * N

stack = []
for a in range(N):
    while stack and stack[-1][0] < A[a]:
        val, idx = stack.pop()
        nge[idx] = A[a]
    stack.append([A[a], a])
print(*nge)