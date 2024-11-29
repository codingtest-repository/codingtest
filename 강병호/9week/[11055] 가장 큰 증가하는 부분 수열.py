
'''
* Author    : BYEONGHO KANG
* Date      : 2024.11.29(Fri)
* Runtime   : 88 ms
* Memory    : 31120 KB
* Algorithm : 다이나믹 프로그래밍
'''

N = int(input())
A = list(map(int, input().split()))

dp = [0] * N

def sol(N:int, A:list):
    
    for i in range(N):
        dp[i] = A[i]
    
    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + A[i])
    
    return max(dp)


print(sol(N, A))
