'''
* Author    : Jang Woo Jin
* Date      : 2024.09.29(Sun)
* Runtime   : 960 ms
* Memory    : 224852 KB(PyPy3)
* Algorithm : data structure
'''

import sys
input = sys.stdin.readline

string = input().strip()
explode = input().strip()
stack = []

for s in string:
    stack.append(s)
    while stack and ''.join(map(str, stack[-len(explode):])) == ''.join(map(str, explode)):
        for i in range(len(explode)):
            stack.pop()

if stack:
    print(''.join(map(str, stack)))
else:
    print("FRULA")