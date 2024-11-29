'''
* Author    : JUYEONG HA
* Date      : 2024.11.29(Fri)
* Runtime   : 272 ms
* Memory    : 54188 KB
* Algorithm : GRAPH
'''

import sys

input = sys.stdin.readline

n = int(input())
bridges = []
tree = [[] for _ in range(n+1)]

for _ in range(n-1): # 간선을 입력받아 트리 생성
    a, b = map(int, input().split())
    bridges.append([a, b])
    tree[a].append(b)
    tree[b].append(a)


q = int(input())
for _ in range(q):
    question, index = map(int, input().split())
    if question == 1: # 단절점
        if len(tree[index]) >= 2: 
            print("yes")
        else:
            print("no")
    else: # 단절선
        print("yes")
