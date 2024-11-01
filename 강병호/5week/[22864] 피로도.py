'''
* Author    : BYEONGHO KANG
* Date      : 2024.11.1(Fri)
* Runtime   : 32 ms
* Memory    : 31120 KB
* Algorithm : 구현
'''

# work per 1h : 피로도 A +, work B -
# 1시간 휴식 : 피로도 C - not minus
# 최대 피로도 M

A, B, C, M = input().split()

A = int(A)
B = int(B)
C = int(C)
M = int(M)

# initialize
fatigue = 0
work = 0

for hour in range(24):
    if fatigue + A <= M:
        fatigue += A
        work += B
    else :
        fatigue = max(0, fatigue - C)
print(work)
