'''
* Author    : BYEONGHO KANG
* Date      : 2024.11.22(Fri)
* Runtime   : 568 ms
* Memory    : 36240 KB
* Algorithm : BruteForce, BackTracking
'''

import itertools
import sys

input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split(' ')))
iter_cnt_list = list(map(int, input().split(' ')))

iterator = ['+', '-', '*', '/']

iterator_set = []
for i in range(4):
    for _ in range(iter_cnt_list[i]):
        iterator_set.append(iterator[i])

iter_order_lst = set(itertools.permutations(iterator_set, N-1))

init_num = arr[0]


min_num = sys.maxsize
max_num = -sys.maxsize

for iter_orders in iter_order_lst:
    result = init_num
    for i, elem in enumerate(iter_orders):
        if elem == '+':
            result += arr[i+1]
        elif elem == '-':
            result -= arr[i+1]
        elif elem == '*':
            result *= arr[i+1]
        elif elem == '/' and result > 0:
            result //= arr[i+1]
        elif elem == '/' and result < 0:
            result = -(abs(result) // arr[i+1])

    if min_num > result:
        min_num = result
    if max_num < result:
        max_num = result


print(max_num)
print(min_num)
