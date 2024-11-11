'''
* Author    : Jang Woo Jin
* Date      : 2024.11.08(Fri)
* Runtime   : 608 ms
* Memory    : 55712 KB
* Algorithm : Dynamic Programming
'''

import sys
input = sys.stdin.readline

String1 = input().strip()
String2 = input().strip()
lenString1 = len(String1)
lenString2 = len(String2)

dp = [[0] * (lenString1+1) for _ in range(lenString2+1)]

for i in range(1, lenString2+1):
    for j in range(1, lenString1+1):
        if String2[i-1] == String1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])