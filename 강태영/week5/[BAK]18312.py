'''
* Author    : 강태영
* Date      : 2024.10.28(MON)
* Runtime   : 100 ms
* Memory    : 31120 KB
* Algorithm : 구현

https://www.acmicpc.net/problem/18312
시각(브론즈2)
'''
import sys
input = sys.stdin.readline

N, K = map(int, (input().split()))

count = 0
str_K = str(K)

for H in range(N+1):
    for M in range(60):
        for S in range(60):
            str_H = str(H)
            str_M = str(M)
            str_S = str(S)
            if H < 10:
                str_H = '0' + str(H)
            if M < 10:
                str_M = '0' + str(M)
            if S < 10 :
                str_S = '0' + str(S)

            if (str_K in str_H) or (str_K in str_M) or (str_K in str_S) :
                count += 1

print(count)