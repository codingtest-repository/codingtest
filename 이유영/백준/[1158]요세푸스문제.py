'''
* Author    : Yooyoung Lee
* Date      : 2024.10.15(Tues)
* Runtime   : 52 ms
* Memory    : 34016 KB
* Algorithm : Queue
'''
from collections import deque

n, k = map(int, input().split())
queue = deque([i for i in range(1, n + 1)])

print('<', end='')
while queue:
    m = k % len(queue)
    queue.rotate(-(m - 1))
    popped = queue.popleft()
    print(popped, end=', ') if queue else print(popped, end='>')
