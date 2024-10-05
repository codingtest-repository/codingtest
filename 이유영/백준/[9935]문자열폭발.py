'''
* Author    : Yooyoung Lee
* Date      : 2024.10.03(Thur)
* Runtime   : 620 ms
* Memory    : 42300 KB
* Algorithm : Stack
'''
import sys
input = sys.stdin.readline

S = input().rstrip()
bomb = input().rstrip()
stack = []
bomb_len = len(bomb)

for s in S:
    stack.append(s)
    if ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()

print('FRULA') if not stack else print(''.join(stack))
