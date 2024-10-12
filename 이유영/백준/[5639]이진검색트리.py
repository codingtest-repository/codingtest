'''
* Author    : Yooyoung Lee
* Date      : 2024.10.11(Fri)
* Runtime   : 1928 ms
* Memory    : 33548 KB
* Algorithm : Recursive(풀이 참고)
* Note      : 풀이 참고, 리스트 슬라이싱 활용하니 시간초과 발생
'''
import sys

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 9)

tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break


def visit(start, end):  # [시작, 끝]
    if start > end:
        return

    div_idx = end + 1
    for i in range(start + 1, end + 1):
        if tree[i] > tree[start]:
            div_idx = i
            break

    visit(start + 1, div_idx - 1)  # left tree
    visit(div_idx, end)  # right tree
    print(tree[start])  # root


visit(0, len(tree) - 1)
