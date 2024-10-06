'''
* Author    : Jang Woo Jin
* Date      : 2024.10.04(Fri)
* Runtime   : 32 ms
* Memory    : 31120 KB
* Algorithm : recursive, tree
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

K = int(input())
tree = [[] for _ in range(K)]
building = list(map(int, input().split()))

def func(start, end, depth):
    if start == end:
        tree[depth].append(building[start])
        return
    mid = (start + end) // 2
    tree[depth].append(building[mid])
    func(start, mid-1, depth+1)
    func(mid+1, end, depth+1)

func(0, len(building)-1, 0)
for i in tree:
    for j in i:
        print(j, end=" ")
    print()