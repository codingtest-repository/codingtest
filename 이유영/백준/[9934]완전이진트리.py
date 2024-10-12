'''
* Author    : Yooyoung Lee
* Date      : 2024.10.09(Wed)
* Runtime   : 52 ms
* Memory    : 34028 KB
* Algorithm : BFS
'''
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
order = list(map(int, input().split()))

queue = deque()
queue.append((0, len(order) - 1))  # [시작, 끝]

while queue:
    size = len(queue)  # 레벨별 출력 위해

    while size > 0:
        start, end = queue.popleft()

        mid = (end + start) // 2
        print(order[mid], end=" ")

        if start <= mid - 1:  # left tree
            queue.append((start, mid - 1))
        if mid + 1 <= end:  # right tree
            queue.append((mid + 1, end))

        size -= 1

    print()
