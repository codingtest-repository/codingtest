'''
* Author    : Jang Woo Jin
* Date      : 2024.10.04(Fri)
* Runtime   : 820 ms
* Memory    : 84508 KB
* Algorithm : data structure
'''

import sys
input = sys.stdin.readline

N = int(input())
circles = []
for i in range(N):
    a, b = map(int, input().split())
    circles.append([a-b, i])
    circles.append([a+b, i])
circles.sort()

stack = []
for circle in circles:
    if not stack:
        stack.append(circle)
    else:
        if stack[-1][1] == circle[1]:
            stack.pop()
        else:
            stack.append(circle)

if stack:
    print("NO")
else:
    print("YES")