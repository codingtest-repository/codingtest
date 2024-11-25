'''
* Author    : Jang Woo Jin
* Date      : 2024.11.22(Fri)
* Runtime   : 60 ms
* Memory    : 31120 KB 
* Algorithm : Backtracking
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
A = list(map(int, input().split()))
operation = list(map(int, input().split()))

MAX = -float("inf") 
MIN = float("inf") 

def recur(idx, result):
    global MAX, MIN
    if idx == N:
        MAX = max(MAX, result)
        MIN = min(MIN, result)
    
    if operation[0] > 0:
        operation[0] -= 1
        recur(idx + 1, result + A[idx])
        operation[0] += 1
    if operation[1] > 0:
        operation[1] -= 1
        recur(idx + 1, result - A[idx])
        operation[1] += 1
    if operation[2] > 0:
        operation[2] -= 1
        recur(idx + 1, result * A[idx])
        operation[2] += 1
    if operation[3] > 0:
        operation[3] -= 1
        recur(idx + 1, int(result / A[idx]))
        operation[3] += 1

recur(1, A[0])
print(MAX)
print(MIN)