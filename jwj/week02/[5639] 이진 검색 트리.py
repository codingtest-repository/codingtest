'''
* Author    : Jang Woo Jin
* Date      : 2024.10.11(Fri)
* Runtime   : 1924 ms
* Memory    : 33548 KB
* Algorithm : recursive, tree
'''

import sys
sys.setrecursionlimit(10**6)    # 최대 재귀 깊이 설정
input = sys.stdin.readline

# 트리 전위 순회 순서 : 루트 → 왼쪽 → 오른쪽
# 트리 후위 순회 순서 : 왼쪽 → 오른쪽 → 루트

tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break

def search(start, end):
    if start > end:
        return
    ridx = end + 1
    for idx in range(start+1, end+1):   # 루트를 제외한 범위 탐색
        if tree[start] < tree[idx]:
            ridx = idx
            break
    search(start+1, ridx-1)    # 왼쪽 서브트리
    search(ridx, end)          # 오른쪽 서브트리
    print(tree[start])         # 루트 노드

search(0, len(tree) - 1)