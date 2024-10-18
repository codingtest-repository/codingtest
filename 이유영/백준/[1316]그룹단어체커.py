'''
* Author    : Yooyoung Lee
* Date      : 2024.10.15(Tues)
* Runtime   : 36 ms
* Memory    : 31252 KB
* Algorithm : Bruteforce
'''
import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    present = set()
    prev = '0'
    for cur in word:
        if cur != prev and cur in present:
            break
        present.add(cur)
        prev = cur
    else:
        cnt += 1

print(cnt)
