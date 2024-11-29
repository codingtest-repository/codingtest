'''
* Author    : BYEONGHO KANG
* Date      : 2024.11.29(Fri)
* Runtime   : 196 ms
* Memory    : 31824 KB
* Algorithm : 구현, 시뮬레이션
'''
import sys
input = sys.stdin.readline

n = int(input())
graph = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u] += 1
    graph[v] += 1

q = int(input())

for _ in range(q):
    t, k = map(int, input().split())
    
    if t == 1:
        print("yes" if graph[k] >= 2 else "no")
    else:
        print("yes")
