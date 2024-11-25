'''
* Author    : BYEONGHO KANG
* Date      : 2024.11.22(Fri)
* Runtime   : 344 ms
* Memory    : 31120 KB
* Algorithm : BruteForce, BackTracking
'''
import itertools

N, S = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))

answer = 0

part_set_arr = []

for i in range(1, N+1):
    part_set_arr = itertools.combinations(arr, i)

    for elem in part_set_arr:
        if sum(elem) == S:
            answer+=1


print(answer)