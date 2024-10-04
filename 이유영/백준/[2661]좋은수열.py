'''
* Author    : Yooyoung Lee
* Date      : 2024.10.03(Thur)
* Runtime   : 40 ms
* Memory    : 31120 KB
* Algorithm : Backtracking
'''
import sys
sys.setrecursionlimit(10 ** 5)


def is_good(s):
    # 전체 길이의 절반까지 확인
    for k in range(1, len(s) // 2 + 1):
        if s[-(2 * k):-k] == s[-k:]:
            return False
    return True


def dfs(cur):
    if len(cur) == n:
        print(cur)
        exit()

    for i in '123':
        nxt = cur + i
        if is_good(nxt):
            dfs(nxt)


n = int(input())
dfs('')
