import sys

input = sys.stdin.readline

n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)

def max_profit(n, schedule):

    for i in range(n - 1, -1, -1):
        time, profit = schedule[i]
        if i + time <= n:
            dp[i] = max(dp[i + 1], profit + dp[i + time])
        else:
            dp[i] = dp[i + 1]

    return dp[0]


print(max_profit(n, schedule))
