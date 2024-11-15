'''
* Author    : Jang Woo Jin
* Date      : 2024.11.15(Fri)
* Runtime   : 116 ms
* Memory    : 35692 KB 
* Algorithm : BruteForce
'''

from itertools import permutations
import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
weight_kit = list(map(int, input().strip().split()))
cnt = 0

for i in list(permutations(weight_kit, len(weight_kit))):
    total_weight = 500
    for j in i:
        total_weight += j
        total_weight -= K
        if total_weight < 500:
            break
    else:
        if total_weight >= 500:
            cnt += 1
print(cnt)