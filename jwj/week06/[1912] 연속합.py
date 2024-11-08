'''
* Author    : Jang Woo Jin
* Date      : 2024.11.08(Fri)
* Runtime   : 88 ms
* Memory    : 38828 KB
* Algorithm : Dynamic Programming
'''

import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().strip().split()))

for i in range(1, n):
    li[i] = max(li[i], li[i-1] + li[i])
print(max(li))