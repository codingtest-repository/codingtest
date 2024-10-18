'''
* Author    : Yooyoung Lee
* Date      : 2024.10.16(Wed)
* Runtime   : 156 ms
* Memory    : 30840 KB
* Algorithm : DP
'''
n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
