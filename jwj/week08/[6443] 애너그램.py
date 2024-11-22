'''
* Author    : Jang Woo Jin
* Date      : 2024.11.22(Fri)
* Runtime   : 612 ms
* Memory    : 31120 KB 
* Algorithm : Backtracking
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

def recur(idx, comb):
    if idx == len(word):
        print(''.join(map(str, comb)))
        return

    prev = None                     # 이전 문자열
    for i in range(len(word)):
        if not visited[i]:
            curr = word[i]
            if prev != curr:        # 이전 문자열과 비교하여 중복 여부를 검증
                visited[i] = True
                comb.append(word[i])
                recur(idx + 1, comb)
                comb.pop()
                visited[i] = False
                prev = curr         # 현재 문자열을 이전 문자열로 갱신

for _ in range(N):
    word = sorted(input().strip())
    visited = [False] * (len(word) + 1)
    recur(0, [])