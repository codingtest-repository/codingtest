'''
* Author    : SHIM SOMIN
* Date      : 2024.10.16(Wed)
* Runtime   : 784 ms
* Memory    : 31120 KB
* Algorithm : 다이나믹 프로그래밍
'''
n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n  

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:  # 증가하는 관계일 때
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))