'''
* Author    : Jang Woo Jin
* Date      : 2024.11.29(Fri)
* Runtime   : 248 ms
* Memory    : 46236 KB 
* Algorithm : Tree(Dictionary)
'''

import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

M = int(input())
for _ in range(M):
    t, k = map(int, input().split())
    if t == 1:
        if len(tree[k]) >= 2:
            print("yes")
        else:
            print("no")
    elif t == 2:
        print("yes")