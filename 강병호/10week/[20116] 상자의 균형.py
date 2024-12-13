'''
* Author    : BYEONGHO KANG
* Date      : 2024.12.06(Fri)
* Runtime   : 208 ms
* Memory    : 56452 KB
* Algorithm : 누적 합
'''
import sys

input = sys.stdin.readline

n, L = map(int, input().split())
x_list = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    prefix_sum[i] = prefix_sum[i + 1] + x_list[i]

is_stable = True

for i in range(n - 1):
    avg = (prefix_sum[i + 1] - prefix_sum[n]) / (n - i - 1)
    if not (x_list[i] - L < avg < x_list[i] + L):
        is_stable = False
        break

print("stable" if is_stable else "unstable")
