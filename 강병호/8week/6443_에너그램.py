'''
* Author    : BYEONGHO KANG
* Date      : 2024.11.22(Fri)
* Runtime   : 428 ms
* Memory    : 31120 KB
* Algorithm : String, BackTracking
'''

import itertools

N = int(input())

input_str = []

for _ in range(N):
    import sys
    input = sys.stdin.readline().rstrip()

    input_str.append(input)


def backtrack(word, used, current):
    if len(current) == len(word):
        print(''.join(current))
        return
    
    for i in range(len(word)):
        if not used[i]:
            if i > 0 and word[i] == word[i-1] and not used[i-1]:
                continue
            used[i] = True
            current.append(word[i])
            backtrack(word, used, current)
            used[i] = False
            current.pop()


def solution(input_str):

    for word in input_str:
        word = sorted(word)
        used = [False] * len(word)
        backtrack(word, used, [])


solution(input_str)