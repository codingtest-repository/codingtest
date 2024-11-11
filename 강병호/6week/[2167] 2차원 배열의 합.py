'''
* Author    : BYEONGHO KANG
* Date      : 2024.11.8(Fri)
* Runtime   : 108 ms
* Memory    : 38752 KB
* Algorithm : 구현, 누적합
'''

import sys
input = sys.stdin.read

data = input().splitlines()

n, m = map(int, data[0].split())

array = []
for i in range(1, n + 1):
    array.append(list(map(int, data[i].split())))

k = int(data[n + 1])

results = []

prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix_sum[i][j] = array[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

for q in range(k):
    i, j, x, y = map(int, data[n + 2 + q].split())
    result = prefix_sum[x][y] - prefix_sum[i - 1][y] - prefix_sum[x][j - 1] + prefix_sum[i - 1][j - 1]
    results.append(result)

for result in results:
    print(result)