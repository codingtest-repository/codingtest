


# N, K = map(int, input().split(' '))

# dp = [0] * 10001
# used = [False] * 10001

# arr = []
# coins = list()
# for _ in range(N):
#     coin = int(input())
#     coins.append(coin)

# coins.sort()
# min_coin_num = 0

# for i in range(K+1):
#     if dp[i] != 0:
#         continue
    
#     for data in coins:
#         if i + data > K : continue
#         elif i + data == K:
#             dp[i + data] = dp[i] + 1
#             used[i + data] = True
#             break
#         elif i + data < K and not used[i+data]:
#             dp[i + data] = dp[i] + 1
#             used[i + data] = True


# for _ in range(20):
#     print(f'dp[{_}] : {dp[_]}')

# print(dp[K])


n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [10001] * (k + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k] if dp[k] < 10001 else -1)

