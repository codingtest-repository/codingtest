'''
* Author    : Jang Woo Jin
* Date      : 2024.10.13(Sun)
* Runtime   : 1876 ms
* Memory    : 34148 KB
* Algorithm : datastructure
'''

import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
q = deque(i for i in range(1, N+1))

result = []
while q:
    for i in range(K-1):
        q.append(q.popleft())        
    v = q.popleft()
    result.append(str(v))

print("<" + ', '.join(result) + ">")