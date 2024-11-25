'''
* Author    : Jang Woo Jin
* Date      : 2024.11.22(Fri)
* Runtime   : 452 ms
* Memory    : 31120 KB 
* Algorithm : Backtracking
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, S = map(int, input().split())
lst = list(map(int, input().split()))

ans = []
tot = 0
def recur(idx):
    global tot
    if sum(ans) == S and len(ans) > 0:
        tot += 1
    for i in range(idx, N):
        ans.append(lst[i])
        recur(i + 1)
        ans.pop()

recur(0)
print(tot)