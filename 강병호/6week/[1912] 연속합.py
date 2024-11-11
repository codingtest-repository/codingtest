'''
* Author    : BYEONGHO KANG
* Date      : 2024.11.6(Thu)
* Runtime   : 84 ms
* Memory    : 39120 KB
* Algorithm : Dynamic Programming
'''

import sys
input = sys.stdin.read

data = input().splitlines()
n = int(data[0])
arr = list(map(int, data[1].split()))

dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])

print(max(dp))