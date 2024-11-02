'''
* Author    : 강태영
* Date      : 2024.11.02(SAT)
* Runtime   : 1084 ms
* Memory    : 31120 KB
* Algorithm : 브루트포스 알고리즘

https://www.acmicpc.net/problem/2231
분해합(브론즈2)
'''

import sys
input = sys.stdin.readline

N = int(input())

result = 0
for i in range(N):
    split_sum = i + sum(map(int, str(i)))
    
    if split_sum == N:
        result = i
        break

print(result)
