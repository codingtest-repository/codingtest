'''
* Author    : Jang Woo Jin
* Date      : 2024.10.28(Mon)
* Runtime   : 2980 ms
* Memory    : 31120 KB
* Algorithm : Brute Force
'''

import sys
input = sys.stdin.readline

N = int(input())
lst = []

for n in range(N-1, 1, -1):
    n = list(str(n))
    tot = int(''.join(map(str, n)))
    for i in range(len(n)):
        tot += int(n[i])
    if tot == N:
        lst.append(''.join(map(str, n)))

if lst:
    lst.sort()
    print(lst[0])
else:
    print(0)