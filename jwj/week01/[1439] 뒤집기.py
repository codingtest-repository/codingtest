'''
* Author    : Jang Woo Jin
* Date      : 2024.09.29(Sun)
* Runtime   : 32 ms
* Memory    : 31120 KB
* Algorithm : Greedy
'''

import sys
input = sys.stdin.readline

S = input().strip()
cnt0 = 0
cnt1 = 0

if S[0] == "0":
    cnt0 += 1
else:
    cnt1 += 1

for i in range(1, len(S)):
    if S[i-1] != S[i]:
        if S[i-1] == "0":
            cnt1 += 1
        else:
            cnt0 += 1
    else:
        continue
print(min(cnt0, cnt1))