'''
* Author    : 강태영
* Date      : 2024.10.29(TUE)
* Runtime   : 32ms
* Memory    : 31120MB
* Algorithm : 구현

https://www.acmicpc.net/problem/22864
피로도(브론즈2)
'''

import sys
input = sys.stdin.readline

def work_and_tired():
    A, B, C, M = map(int, input().split())
    
    tired = 0
    work = 0
    result = 0

    for i in range(24):
        if tired > M:
            result = 0
            return result
        else:
            if tired + A <= M:
                tired += A
                work += B
            else:
                if tired - C < 0:
                    tired = 0
                else:
                    tired -= C

    return work

print(work_and_tired())