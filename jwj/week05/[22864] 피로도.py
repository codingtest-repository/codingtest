'''
* Author    : Jang Woo Jin
* Date      : 2024.10.28(Mon)
* Runtime   : 32 ms
* Memory    : 31120 KB
* Algorithm : Brute Force
'''

import sys
input = sys.stdin.readline

# 한 시간 일하면 피로도는 A만큼 늘어나고 일은 B만큼 처리
# 한 시간 쉬면 피로도는 C만큼 줄어든다.

A, B, C, M = map(int, input().split())

# 피로도 : p
# 처리량 : t

p = 0
t = 0

for h in range(24):
    # 피로도가 M을 넘긴다면?(던져버림)
    if p > M:
        print(0)
        sys.exit(0)
    else:
        if p + A <= M:
            p += A
            t += B
        else:
            if p - C < 0:
                p = 0
            else:
                p -= C
print(t)