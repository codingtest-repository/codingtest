'''
* Author    : Yooyoung Lee
* Date      : 2024.10.12(Sat)
* Runtime   : 596 ms
* Memory    : 78364 KB
* Algorithm : Stack
* Note      : 풀이 참고(스택 활용 아이디어 떠오르지 X)
'''
import sys
input = sys.stdin.readline

n = int(input())

circles = []

for k in range(n):
    x, r = map(int, input().split())
    circles.append((x - r, k))
    circles.append((x + r, k))

circles.sort()

stack = []
for circle in circles:
    if stack:
        if stack[-1][1] == circle[1]:
            stack.pop()
        else:
            stack.append(circle)
    else:
        stack.append(circle)

if stack:
    print("NO")
else:
    print("YES")
