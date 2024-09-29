'''
* Author    : Jang Woo Jin
* Date      : 2024.09.29(Sun)
* Runtime   : 36 ms
* Memory    : 31252 KB
* Algorithm : recursive
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
result = []

# 좋은 수열인지 나쁜 수열인지 체크하는 함수
def check(seq):
    good = True
    for idx in range(1, (len(seq) // 2) + 1):
        prev = seq[-idx:]
        comp = seq[-idx*2:-idx]
        if prev == comp:
            good = False
            break
    return good

def backtracking(seq):
    # 종료 조건 - 길이가 N & 좋은 수열
    if len(seq) == N:
        if check(seq):
            print("".join(map(str, seq)))
            sys.exit(0)
    for i in [1, 2, 3]:
        seq.append(i)
        # 좋은 수열인 경우만 백트래킹
        if check(seq):
            backtracking(seq)
        seq.pop()

backtracking([])